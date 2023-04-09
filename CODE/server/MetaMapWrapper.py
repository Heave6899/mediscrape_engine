from pymetamap import MetaMap
import skr_web_api as sk
class MetaMapWrapper(object):
    mm = MetaMap.get_instance('/home/parallels/Desktop/mediscrape/public_mm/bin/metamap20')
    def __init__(self):
        self.key = 'api-key'
        self.email = 'xyz@abc'
        self.subm = sk.Submission(self.email,self.key)
        pass

    def online_annotate(self,text):
        self.subm.init_mm_interactive(text)
        response = self.subm.submit()
        extracted_data = {}
        symptoms = []
        diseases = []
        diagnostics = []
        decoded_body = [i.split('|') for i in response.content.decode().split('\n')]
        for concept in decoded_body:
            if len(concept) > 6:
                if concept[5] == '[sosy]':
                        # Sign or Symptom
                        # sometimes it returns symptoms as a symptom
                    if concept[3] != 'Symptoms' and concept[3] != 'symptoms':
                        symptoms.append(concept[3])
                elif concept[5] == '[dsyn]':
                    # Disease or Syndrome
                    diseases.append(concept[3])
                    pass
                elif concept[5] == '[diap]':
                    # Diagnostic Procedure
                    diagnostics.append(concept[3])
        if len(symptoms):
            extracted_data['symptoms'] = symptoms
        if len(diseases):
            extracted_data['diseases'] = diseases
        if len(diagnostics):
            extracted_data['diagnostics'] = diagnostics

        return extracted_data


    def annotate(self, text):
        mm_request = [text]
        concepts, error = self.mm.extract_concepts(mm_request, [1, 2])
        extracted_data = {}
        symptoms = []
        diseases = []
        diagnostics = []
        for concept in concepts:
            if hasattr(concept, 'semtypes'):
                # print(concept)
                if concept.semtypes == '[sosy]':
                    # Sign or Symptom
                    # sometimes it returns symptoms as a symptom
                    if concept.preferred_name != 'Symptoms' and concept.preferred_name != 'symptoms':
                        symptoms.append(concept.preferred_name)
                elif concept.semtypes == '[dsyn]':
                    # Disease or Syndrome
                    diseases.append(concept.preferred_name)
                    pass
                elif concept.semtypes == '[diap]':
                    # Diagnostic Procedure
                    diagnostics.append(concept.preferred_name)

        if len(symptoms):
            extracted_data['symptoms'] = symptoms
        if len(diseases):
            extracted_data['diseases'] = diseases
        if len(diagnostics):
            extracted_data['diagnostics'] = diagnostics

        return extracted_data
