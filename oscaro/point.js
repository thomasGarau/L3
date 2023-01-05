const fs = require('fs');

const BORDURE_MAX_LONGITUDE = 9.605320;
const BORDURE_MIN_LONGITUDE = 8.461863;
const BORDURE_MAX_LATITUDE = 43.079776;
const BORDUE_MIN_LATITUDE = 41.306198;
const PI = Math.PI;
const cos = Math.cos;
const METTRE = 100;
EARTH = 6378.137;
let m = (1 / ((2 * PI / 360) * EARTH)) / 1000

let new_longitude = BORDURE_MIN_LONGITUDE;
let new_latitude = BORDUE_MIN_LATITUDE;

var obj = {
    listePoint: []
 };


while (new_latitude < BORDURE_MAX_LATITUDE){
    console.log(new_latitude, new_longitude);
    while (new_longitude < BORDURE_MAX_LONGITUDE){
        new_longitude = new_longitude + (METTRE * m) / cos(new_latitude * (PI / 180));
        obj.listePoint.push({
            longitude : new_longitude,
            latitude : new_latitude,
        })
    }
    new_latitude = new_latitude + (METTRE * m);
}

console.log(obj);