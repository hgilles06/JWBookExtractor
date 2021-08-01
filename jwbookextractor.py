from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import numpy as np
import pandas as pd
import os


def GetJWData(book_url):
    
    global driver
    
    df = pd.DataFrame(columns = ["url", "text", "chapter_audio"])
    
    #Launching Chrome driver
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('log-level=3')
    #options.add_argument('--headless')  #with the headless option, no data is found
    
    
    driver=webdriver.Chrome(options=options)
    driver.implicitly_wait(1)
    driver.get(book_url)
    
    chapter_urls = [element.find_element_by_tag_name("a").get_attribute("href") for element in driver.find_elements_by_tag_name("h2")[1:]]
    
    text_list, url_list, audio_list = [], [], []
    
    for chapter_url in chapter_urls:
       
        driver.get(chapter_url)
        title = driver.find_element_by_tag_name("h1").text
        text = [title] + [element.text for element in driver.find_elements_by_tag_name("p") if element.text!=""]
        try:
            audio = driver.find_element_by_css_selector("""#vjs_video_3_html5_api""").get_attribute("src")
        except:
            audio = np.nan
            
        text_list = text_list + text
        url_list = url_list + [chapter_url]*len(text)
        audio_list = audio_list + [audio]*len(text)
        
    df["text"] = text_list
    df["url"] = url_list
    df["chapter_audio"] = audio_list
    
    driver.close()
    
    return df





def SaveSrc(source_url, source_file, save_dir):
    

    print("Data collection")
    
    print("source!")
    
    source_file = save_dir+"/"+source_file
    
    try:
        df_source = GetJWData(source_url)
    except:
        print("Can't get the data!")
        driver.close()
        return None
    
    
    if (not os.path.exists(source_file)): 
        df_source.to_csv(source_file, index=None)
        return "Files created and saving done!"
        
    
    all_df_source = pd.read_csv(source_file)
    all_df_source = pd.concat([all_df_source, df_source], axis=0)
    
    all_df_source = all_df_source.drop_duplicates()
    
    all_df_source.to_csv(source_file, index=None)
    
    print("Concatenation done with the existing data!")
    




def SaveSrcTgt(source_url, target_url, source_file, target_file, save_dir):
    

    print("Data collection")
    
    source_file = save_dir+"/"+source_file
    target_file = save_dir+"/"+target_file
    
    
    
    try:
        print("source!")
        df_source = GetJWData(source_url)
    
        print("target!")
        df_target =  GetJWData(target_url)
    
    except:
        print("Can't get the data!")
        driver.close()
        return None
    
    if df_source.shape!=df_target.shape:
        print("Shapes are not matching")
        driver.close()
        return None

    
    if (not os.path.exists(source_file))|(not os.path.exists(target_file)): 
        df_source.to_csv(source_file, index=None)
        df_target.to_csv(target_file, index=None)
        print("Files created and saving done!")
        driver.close()
        return None
        
        
   
    all_df_source = pd.read_csv(source_file)
    all_df_target = pd.read_csv(target_file)
        
    all_df_source = pd.concat([all_df_source, df_source], axis=0)
    all_df_target = pd.concat([all_df_target, df_target], axis=0)
    
    all_df_source = all_df_source.drop_duplicates()
    all_df_target = all_df_target.drop_duplicates()
    
    all_df_source.to_csv(source_file, index=None)
    all_df_target.to_csv(target_file, index=None)
    
    print("Concatenation done with the existing data!")
    
    