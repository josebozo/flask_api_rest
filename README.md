# flask_api_rest
Aplicaciones para test de comunicacion de entornos, despliegues y comunicacion 

Primer commit:
	Dos rest en flask que almacenan key/value en redis

	rest_add: almacena key/value en redis
	comando: curl -i -H "Content-Type: application/json" -X POST -d '{"key":"<key>","value":"<value>"}' http://localhost:5000/todo/api/add


	rest_read: lectura de key/value almacenada en redis
	comando: curl -i  http://localhost:5001/todo/api/read/<key>


Para despliegue rapido ejecutamos "docker-compose up" 
Empaquetara y desplegara el conjunto de elementos para su uso.

En caso que se dese reconstruir la imagen en cada despliegue "docker-compose up --build"
