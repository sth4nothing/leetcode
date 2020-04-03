class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        try:
            if '.' in IP:
                # IPv4
                strs = IP.split('.')
                if len(strs) == 4:
                    for s in strs:
                        if not s or len(s) > 1 and s[0] == '0' or not 0 <= int(s) < 256 or s[0] in '+-':
                            break
                    else:
                        return 'IPv4'
            elif ':' in IP:
                # IPv6
                omit = None
                strs = IP.split(':')
                if len(strs) == 8:
                    for s in strs:
                        if not s or len(s) > 4 or not 0 <= int(s, 16) <= 0xffff or s[0] in '+-':
                            break
                    else:
                        return 'IPv6'
        except ValueError:
            pass
        return 'Neither'
