drop table if exists monkey;
create table monkey(
	user_id integer primary key autoincrement,
	user_name text not null,
	email text not null,
	pw_hash text not null
);

