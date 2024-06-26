from importers import *


@app.get("/corporate_data/companyinfo/{isin}")
def get_company_info(request: Request, response: Response, isin: str):
    results = db_.exec_stored_procedure(
        db_conn_,
        "public.get_company_data",
        [
            isin
        ]
    )
    return results[0][0][0]
