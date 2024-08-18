function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.bathrooms = values[0];
    obj.bedrooms = values[1];
    obj.city = values[2];
    obj.country = values[3];
    obj.homeStatus = values[4];
    obj.homeType = values[5];
    obj.latitude = values[6];
    obj.longitude = values[7];
    obj.livingArea = values[8];
    obj.lotAreaUnit = values[9];
    obj.lotAreaValue = values[10];
    obj.price = values[11];
    obj.rentZestimate = values[12];
    obj.state = values[13];
    obj.zipcode = values[14];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }
