class EmailValidator:

    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains


    def __is_name_valid(self, name: str):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str):
        return mail in self.mails

    def __is_domain_valid(self, domain: str):
        return domain in self.domains


    def validate(self, email):
        user, emails = email.split('@')
        mail, domain = emails.split('.')

        return self.__is_domain_valid(domain) and self.__is_mail_valid(mail) and self.__is_name_valid(user)
    



ev = EmailValidator(5, ["me"], ["you", "he"])
print(ev.validate("itsme@me.you"))#, True
print(ev.validate("me@me.you"))#, False
print(ev.validate("itsme@me.she"))#, False
print(ev.validate("itsme@you.he"))#, False
print(ev._EmailValidator__is_domain_valid("he"))#, True)
print(ev._EmailValidator__is_domain_valid("she"))
print(ev._EmailValidator__is_mail_valid("me"))
print(ev._EmailValidator__is_mail_valid("you"))
print(ev._EmailValidator__is_mail_valid("abc"))
print(ev._EmailValidator__is_mail_valid("abcdef"))