import numpy as np

from env import user, password, host
from utilities import generate_db_url, generate_df

def _acquire_telco(cached=True):
    telco_query = """
    SELECT *
           FROM customers
               JOIN contract_types USING(contract_type_id)
               JOIN internet_service_types USING(internet_service_type_id)
               JOIN payment_types USING(payment_type_id);
    """
    
    return generate_df("telco_churn.csv", telco_query, generate_db_url(user, password, host, "telco_churn"), cached)

def _clean_telco(telco_df):
    clean_df = telco_df.copy()
    
    # Only want two year contracts
    two_year_customers = clean_df[clean_df.contract_type == "Two year"]
    
    # Only need these columns
    two_year_customers = two_year_customers[['customer_id', 'monthly_charges', 'tenure', 'total_charges']]
    
    # Replace empty total charges with 0 since need 1 month of tenure to incur charges
    two_year_customers.total_charges = two_year_customers.total_charges.replace(" ", np.nan)
    two_year_customers = two_year_customers.fillna(0)
    
    # Change total charges to float
    two_year_customers.total_charges = two_year_customers.total_charges.astype(float)
    
    # Set index to customer ID
    two_year_customers = two_year_customers.set_index('customer_id')
    
    return two_year_customers

def wrangle_telco():
    return _clean_telco(_acquire_telco())
    