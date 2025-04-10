
 
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
    function createPatient(patient, callback){
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
    function updatePatient(patient, callback){
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
    function deletePatient(id, callback){
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
            
            displaypatient = {}
            displaypatient.id = patient.id
            displaypatient.name = patient.name
            displaypatient.age = patient.age
            displaypatient.type_of_treatment = patient.type_of_treatment
            
            console.log(displaypatient)
        }
    }
     getAll(processGetAllResponse)

     ///// Create
    function processCreateResponse(result){
        console.log(result)
    }
    //patient = {"Id":"javascript", "Name":"John","Age":88,"type_of_treatment":"HDF"} 
    //createPatient(patient,processCreateResponse) 

    //// update
    function processUpdateResponse(result){
        console.log(result)
    }
    //patient = {"Id":"javascript","Name":"John","Age":88, "type_of_treatment":"HDF"} 
    //updatePatient(patient,processUpdateResponse)
    
    ////delete
    
    function processDeleteResponse(result){
        console.log("in process delete")
        console.log(result)
    }
    //deletePatient(1,processDeleteResponse) 