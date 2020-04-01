# My_Project
  A Toolset For Automated Detection of Cross-Site Scripting Vulnerablilities in Web Applications
  
  Major Steps of this Tool are as follows:
  
  1. Input is a website (url)
  
  2. Extract Forms and submit these forms with payloads added in the GET parameters
  
  3. Analysis of the Response against Form Submissions, extracts XSS-context data
  
  4. Analysis of the Contexts obtained
    
      a. Encoding Anaylysis
    
      b. Filtering Analysis
    
      c. Attack Methodology
    
      d. Selection of Payloads
  
  5. After selecting Attack-Mehtodology and Attack-Payloads, attacks the webpage with new payloads
  
  6. Analyzes the Response against Attack-Payloads to find out if the attack was successful or NOT

Data Extracted From Website:
  
  1. GET Urls (with Payloads): [ https://www.zentechnologies.com/search/search.php?query="xyz'yxz</zxy&search=1 ]
  
  2. No. of GET Urls: e.g: [2] 
  
  3. Context Data : 
      
      a. Attribute
      
      b. HTML
      
      c. Script
      
      d. URL 
      
      e. Same Attribute
      
      f. Same HTML
      
      g. Same Script
      
      h. Same URL
   
   4. Encoding Analysis: 
      
      a. Single Quotes
      
      b. Double Quotes
      
      c. Less-than sign
      
      d. Forward Slash
      
   5. Selected Attack-Payloads: e.g: ["'; confirm(1); '"]
   
   6. Attack URL: e.g: 
   
   SCRIPT Attack Url:  https://www.nearlynatural.com/collections/search-results?type=product&keywords='; confirm(1); '
   
   7. Success of Attack: e.g: [UnSuccessful with payload:  '; confirm(1); ']
   
   
   .....
