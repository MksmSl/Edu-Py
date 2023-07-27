CREATE TABLE user_type (
    id serial PRIMARY KEY,
    type VARCHAR(50) NOT NULL
);


CREATE TABLE users (
    id serial PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(30) NOT NULL,
    user_type_id int NOT NULL,
    
    FOREIGN KEY (user_type_id)
        REFERENCES user_type (id)
	);

CREATE TABLE attributes (
    id serial PRIMARY KEY,
    attribute VARCHAR(50) NOT NULL
);


CREATE TABLE rooms (
    id serial PRIMARY KEY,
    room VARCHAR(50) NOT NULL,
    res_amount int NOT NULL,
    price int NOT NULL,
    first_day timestamp NOT NULL,
    last_day timestamp NOT NULL,
    host_id int NOT NULL,
    
    FOREIGN KEY (host_id)
        REFERENCES users (id)
	);

CREATE TABLE attribute_room (
    id serial PRIMARY KEY,
    room_id int NOT NULL,
    attribute_id int NOT NULL,

    FOREIGN KEY (room_id)
        REFERENCES rooms (id),
    FOREIGN KEY (attribute_id )
        REFERENCES attributes (id)
	);
   
CREATE TABLE room_reservation (
    id serial PRIMARY KEY,
    room_id int NOT NULL,
    from_date timestamp NOT NULL,
    "to_date" timestamp NOT NULL,
    user_id int NOT NULL,
    guest_amount int NOT NULL,
    
    FOREIGN KEY (room_id)
        REFERENCES rooms (id),
    FOREIGN KEY (user_id)
        REFERENCES users (id)   
	);

INSERT INTO user_type("type") 
	VALUES ('guest'), ('host');

INSERT INTO public.users(name, email, user_type_id) 
	VALUES ('John Smith', 'js1@mail', 2), 
		('John Smith2', 'js2@mail', 1),
		('John Smith3', 'js3@mail', 1);

INSERT INTO public."attributes"("attribute") 
	VALUES ('A/C'), ('refrigerator '), ('fan');

INSERT INTO public.rooms (room, res_amount, price, first_day, last_day, host_id)
	VALUES ('London, avenu 21', 2, 100, '2023-02-12', '2024-02-12', 1),
			('Paris, avenu 23', 3, 300, '2023-03-02', '2024-03-02', 1),
			('Berlin, avenu 24', 1, 250, '2023-03-20', '2024-03-20', 1);	
		
INSERT INTO public.attribute_room (room_id, attribute_id) 
	VALUES (1,1), (1,2), (1,3), (2,1), (2,2), (3,1) ;

INSERT INTO public.room_reservation (room_id, from_date, to_date, user_id, guest_amount) 
	VALUES (1, '2023-04-10', '2023-04-20', 2, 2),
			(2, '2023-05-05', '2023-05-15', 2, 3),
			(3, '2023-06-01', '2023-06-15', 3, 1);


SELECT COUNT(*) as res_count, u."name" 
FROM room_reservation
JOIN users u ON user_id = u.id
GROUP BY user_id, u."name" 
ORDER BY res_count DESC 
LIMIT 1


