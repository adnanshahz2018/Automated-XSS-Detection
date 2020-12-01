

class direct_get_params:
    payload = 'abc/uvw"' + "xyz'yxz<zxy"
    paramvalues = {}

    def start(self, url):
        params = {}
        get_params = []

        url = str(url)
        part = url.split('?')
        pairs = part[1].split('&')

        if len(pairs) > 1:
            for pair in pairs:
                p = pair.split('=')
                if len(p) == 2:
                    if p[1]:    params[p[0]] = p[1]
                    else:   params[p[0]] = ''
                else:   params[p[0]] = ''
        else:   
            p = pairs[0].split('=')
            if len(p) == 2:
                if p[1]:    params[p[0]] = p[1]
                else:   params[p[0]] = ''
            else:   params[p[0]] = ''

        self.paramvalues = params.copy()
        for p in params: get_params.append(p)
        print('\nparams = ', get_params, '\n')

        links = self.add_payload(part[0], params)

        return  get_params, links

    def add_payload(self, part, params):
        links = []

        for p in params:
            params[p] = self.payload
            link = self.make_links(part, params)
            links.append(link)
            params = self.paramvalues.copy()
        
        # for link in links:  print(link)

        return links

    def make_links(self, part, params):
        data = part + '?'
        for p in params:
            if params[p] and p: data += p + '=' + params[p] + '&' 
            elif p: data += p + '=' + '' + '&'
        form_data = data[:-1]
        # print('form-data = ', form_data)
        return form_data


if __name__ == "__main__":

#   http://db.etree.org/shnlist.php?artist&artist_group_key=1&year=

    pass