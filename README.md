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
