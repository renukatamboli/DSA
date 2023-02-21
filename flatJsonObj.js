// {'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]}
// {
//   a: 1,
//   'c.a': 2,
//   'c.b.x': 3,
//   'c.b.y': 4,
//   'c.b.z': 5,
//   'd.0': 6,
//   'd.1': 7,
//   'd.2': 8
// }

const jsonObj = {'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]}

function flatten(jsonObj={},ObjKey=""){
  for(key in jsonObj){
     if(typeof jsonObj[key] == "object"){
        flatten(jsonObj[key],`${ObjKey}.${key}`)
     }
     else{
       flat = ObjKey+"."+key+":"+jsonObj[key]
       console.log(flat.slice(1))
     }
  }
}

flatten(jsonObj)
