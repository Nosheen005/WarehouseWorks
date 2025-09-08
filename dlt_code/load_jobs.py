 
import dlt
import requests
import json
from pathlib import Path
import os
 
 
def _get_ads(url_for_search, params):
    headers = {"accept": "application/json"}
    response = requests.get(url_for_search, headers=headers, params=params)
    response.raise_for_status() 
    return json.loads(response.content.decode("utf8"))
 
 
@dlt.resource(write_disposition="append")
def jobsearch_resource(params):
    """
    params should include at least:
      - "q": your query
      - "limit": page size (e.g. 100)
      - "occupation-field": the occupation field concept ID
    """
    url = "https://jobsearch.api.jobtechdev.se"
    url_for_search = f"{url}/search"
    limit = params.get("limit", 100)
    offset = 0
 
    while True:
        page_params = dict(params, offset=offset)
        data = _get_ads(url_for_search, page_params)
 
        hits = data.get("hits", [])
        if not hits:
            break
 
        for ad in hits:
            yield ad
 
        if len(hits) < limit or offset > 1900:
            break
 
        offset += limit
 
 
def run_pipeline(query, table_name, occupation_fields):
    pipeline = dlt.pipeline(
        pipeline_name="raw_jobs", 
        destination="snowflake",
        dataset_name="staging",
    )
 
    for occupation_field in occupation_fields:
        params = {"q": query, "limit": 100, "occupation-field": occupation_field}
        load_info = pipeline.run(
            jobsearch_resource(params=params), table_name=table_name
        )
        print(f"Occupation field: {occupation_field}")
        print(load_info)
 
 
if __name__ == "__main__":
    working_directory = Path(__file__).parent
    os.chdir(working_directory)
 
    query = "" 
    table_name = "raw_jobs"
 
    occupation_fields = (
        "X82t_awd_Qyc",   # Administration, ekonomi, juridik
        "j7Cq_ZJe_GkT",   # Bygg och anläggning  
        "apaJ_2ja_LuF"    # Data/IT
    )
 
    run_pipeline(query, table_name, occupation_fields)
 