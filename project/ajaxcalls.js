
 
    function getAll(callback){
        $.ajax({
            "url": "http://127.0.0.1:5000/patient",
            "method":"GET",
            "data":"",
            "dataType": "JSON",
            "success":function(result){
                //console.log(result);
                callback(result)
     
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }

    // testing code
    function createpatient(patient, callback){
        console.log(JSON.stringify(patient));
        $.ajax({
            "url": "http://127.0.0.1:5000/patient",
            "method":"POST",
            "data":JSON.stringify(patient),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                //console.log(result);
                callback(result)  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }
    function updatepatient(patient, callback){
        console.log("updateing " +JSON.stringify(patient));
        $.ajax({
            "url": "http://127.0.0.1:5000/patient/"+encodeURI(patient.id),
            "method":"PUT",
            "data":JSON.stringify(patient),
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                console.log(result);
                callback(result)   
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });
    }
    function deletepatient(id, callback){
        $.ajax({
            "url": "http://127.0.0.1:5000/patient/"+id,
            "method":"DELETE",
            "data":"",
            "dataType": "JSON",
            contentType: "application/json; charset=utf-8",
            "success":function(result){
                console.log(result);
                callback(result)  
            },
            "error":function(xhr,status,error){
                console.log("error: "+status+" msg:"+error);
            }
        });

    }



    // testing code
    
    function processGetAllResponse(result){
        console.log("in process")
        //console.log(result)
        for (patient of result){
            //console.log(patient)
            // issue the format of the patient object is different from lab06.02
            // there are two solutions change the patient object in lan06.02 to have capitals 
            // or convert
            displaypatient = {}
            displaypatient.id = patient.id
            displaypatient.name = patient.name
            displaypatient.age = patient.age
            displaypatient.type_of_treatment = patient.type_of_treatment
            // you can now pass it to addpatientToTable
            console.log(displaypatient)
        }
    }
     getAll(processGetAllResponse)

     ///// Create
    function processCreateResponse(result){
        console.log(result)
    }
    //patient = {"Id":"javascript", "Name":"John","Age":88,"Type of Treatment":"HDF"} 
    //createpatient(patient,processCreateResponse) 

    //// update
    function processUpdateResponse(result){
        console.log(result)
    }
    patient = {"Id":"javascript","Name":"John","Age":88, "Type of treatment":"HDF"} 
    //updatepatient(patient,processUpdateResponse)
    
    ////delete
    
    function processDeleteResponse(result){
        console.log("in process delete")
        console.log(result)
    }
    //deletepatient(1,processUpdateResponse) 