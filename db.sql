--
-- script to create a twitter-like db
--

DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS follows;
DROP TABLE IF EXISTS mentions;
DROP TABLE IF EXISTS tweets;

CREATE TABLE IF NOT EXISTS users(
	user_id int PRIMARY KEY NOT NULL,
	name varchar(20) NOT NULL,
	profile_img_url varchar(200) NOT NULL,
	description varchar(200) DEFAULT NULL,
	create_on timestamp NOT NULL,
	followers_count int NULL
	);

CREATE TABLE IF NOT EXISTS tweets(
	tweet_id int PRIMARY KEY NOT NULL,
	tweet_text varchar(160) NOT NULL,
	created_on timestamp NOT NULL,
	user_id int NOT NULL,
	name varchar(20) NOT NULL,
	profile_img_url varchar(200),
	FOREIGN KEY (user_id) REFERENCES users (user_id)
	);

CREATE TABLE IF NOT EXISTS mentions(
	tweet_id int NOT NULL,
	source int NOT NULL,
	target int NOT NULL,
	FOREIGN KEY (tweet_id) REFERENCES users (user_id),
	FOREIGN KEY (source) REFERENCES users (user_id),
	FOREIGN KEY (target) REFERENCES users (user_id)
	);

CREATE TABLE IF NOT EXISTS follows(
	follower int NOT NULL,
	followed int NOT NULL,
	FOREIGN KEY (follower) REFERENCES users (user_id),
        FOREIGN KEY (followed) REFERENCES users (user_id)
	);
