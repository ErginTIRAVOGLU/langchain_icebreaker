import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url:str, mock:bool=False):
    """
    scrape information from LinkedIn profiles, Manually scrape the information from LinkedIn profile
    """
    
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/ErginTIRAVOGLU/de1c08143b7f29d162c793590d8b5c92/raw/28a337c0e98f9b8b04e0bb6e62c2098bb075442a/ergin-linkedin"
        response = requests.get(
            linkedin_profile_url, 
            timeout=20
        )
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic= {
            "Authorization": f"Bearer {os.getenv('PROXYCURL_API_KEY')}"
        }
        response = requests.get(
            api_endpoint, 
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10
        )
        
    data=response.json()
    data={
        k:v
        for k,v in data.items()
        if v not in ([],"","",None)
        and k not in["people_also_viewed","certifications"]
    }
    
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    with open("linkedin_data.json", "w", encoding="utf-8") as file:
        file.write(response.text)
    return data
    
if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://linkedin.com/in/ergin-tiravoglu/",mock=True
        )
    )