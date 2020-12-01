
# Towards Automated Detection of Cross-Site Scripting  (XSS) Vulnerabilities in Web Applications
  
  INPUT:  Website URL or List of Website URLs
 
  OUTPUT: Summary of Source Code Analysis and XSS Vulnerabilities (if any)
  
  # Major Steps of this Tool are as follows:
  
  1. Collect the source code of the web page
  
  2. Extract Forms and add Harmless String, with special characters, to the GET Parameters
  
  3. Submit Forms with Harmless strings, for probing the web application
  
  4. Collection and Categorization of Response into 4 Contexts: 
    
    a. Attribute 
    
    b. HTML
    
    c. Script
    
    d. URL 
  
  5. Source Code Analysis
  
  6. Selection of Attacks w.r.t Categorization
  
  7. Verify Attack by Analyzing the Response
  
  8. Record Results (Text and Excel Files)
  
  
  

# Data Extracted From Website:
  
  1. GET Urls (with Harmless String): [ https://www.zentechnologies.com/search/search.php?query="xyz'yxz</zxy&search=1 ]
  
  2. No. of GET Urls: e.g: [2] 
  
  3. Context Data : 
      
    a. Attribute
      
    b. HTML
      
    c. Script
      
    d. URL 
      
   
   4. Source Code Analysis for Special Characters: 
      
    a. Single Quotes
      
    b. Double Quotes
      
    c. Less-than sign
      
    d. Forward slash
      
   5. Attacks selected: e.g: ["'; confirm(1); '"]
   
   6. Attack URL: e.g: 
   
    SCRIPT Attack Url:  https://www.nearlynatural.com/collections/search-results?type=product&keywords='; confirm(1); '
   
   7. Verification of Attack: e.g: [UnSuccessful with attack:  '; confirm(1); ']
   
   8. Reflection of Attack in the Response, e.g: attack = {' onmouseover='alert(1)} and {<img src=x onerror="confirm(1)">}
  
  a. ['<input type="hidden" name="query" value="' onmouseover='alert(1)">', '<input type="hidden" name="name" value="'onmouseover='alert(1)" />']
  
  b. ['<q><img src=x onerror="confirm(1)"></q>']
      
   
  # Storage of DATA: 
  
  1. TEXT FILE: (contains following data)
  
    a. Response Categorization: Context frequency and Values
    
    b. Source Code Analysis: For Special Characters
    
    c. Selected Attacks and URLs generated along with these attacks
    
    d. Specifies the Context of Attack
    
    e. Status of the Attacks: Successful or Faliure
    
    f. Detection or Reflection of Attacks in the web application source code
    
    
  2. EXCEL FILE: 
  
    a. Context frequency and Values
    
    b. URLs generated along with the Selected Attacks 
    
    c. Specifies the Context of Attack
    
    d. Verification of Attack: Success or Failure
    
    e. Detection or Reflection of the Attacks in the Response 
    
    
    
    
 #                                                    ------------ THE END ----------------
