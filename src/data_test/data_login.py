class DataLogin:
    title = "ISIIGO"
    title_correct = "Siigo Nube"

    qa_colombia = [{"url": "https://qastaging.siigo.com/", "username": "siigo@techmf.com",
                    "ValidateCompanyName": {"MenuNuevo": False, "CompanyName": "Siigo TechMF"}, "title": title_correct,
                    "ValidateENV": "qastaging"}]
    qa_mexico = [{"url": "http://qastaging.siigo.mx/", "username": "QADesplieguePremium001@yopmail.com",
                  "ValidateCompanyName": {"MenuNuevo": True, "CompanyName": "QADesplieguePremium001"}, "title": title_correct,
                  "ValidateENV": "qastaging"}]
    qa_chile = [{"url": "http://qastaging.siigo.cl/", "username": "admin@eventos.com",
                 "ValidateCompanyName": {"MenuNuevo": True, "CompanyName": "EVENTOS EN LA NUBE"}, "title": title_correct,
                 "ValidateENV": "qastaging"}]
    qa_ecuador = [{"url": "http://qastaging.siigo.ec/", "username": "admin@uno.com",
                   "ValidateCompanyName": {"MenuNuevo": True, "CompanyName": "ALMACEN TODO EN UNO"}, "title": title,
                   "ValidateENV": "qastaging"}]
    canary = [{"url": "https://siigonube.siigo.com/", "username": "calidad_nube@piloto.com",
               "ValidateCompanyName": {"MenuNuevo": False, "CompanyName": "PILOTO  CALIDAD  NUBE 02082022 QC"}
                  , "title": title, "ValidateENV": "siigonube2"}]
