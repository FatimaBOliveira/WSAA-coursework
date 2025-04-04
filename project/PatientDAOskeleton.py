# Patient dao skeleton
# Author: Fatima Oliveira

class PatientDAO:
              
    def getAll(self):
    # get all
        return [{"id":1,"name":"John","age":77,"type_of_treatment": "HDF"}]
    # find by id
    def findByID(self, id):
        return {"id":1,"name":"John","age":77,"type_of_treatment": "HDF"}
    # create a book
    def create(self, patient):
        return {"id":1,"name":"John","age":77,"type_of_treatment": "HDF"}
    # update a book
    def update(self,id , patient):
        return {"id":1,"name":"John","age":77,"type_of_treatment": "HDF"}
    # delete a book of a given id    
    def delete(self, id):
        return True
        
patientDAO = PatientDAO()

if __name__ == "__main__":
    patient = {"id":1,"name":"John","age":77,"type_of_treatment": "HDF"} 
    print ("test getall")
    print (f"\t{patientDAO.getAll()}")
    print ("test findById(1)")
    print (f"\t{patientDAO.findByID(1)}")
    print ("test create")
    print (f"\t{patientDAO.create(patient)}")
    print ("test update")
    print (f"\t{patientDAO.update(1,patient)}")
    print ("test delete")
    print (f"\t{patientDAO.delete(1)}")