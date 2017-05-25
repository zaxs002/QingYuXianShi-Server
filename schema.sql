create database zhitiao;

use zhitiao;

grant select, insert, update, delete on awesome.* to `root`@`localhost` identified by `root`;
	
create table users (
    `id` varchar(50) not null,
    `email` varchar(50) not null,
    `passwd` varchar(50) not null,
    `admin` bool not null,
    `name` varchar(50) not null,
    `image` varchar(500) not null,
    `created_at` real not null,
    unique key `idx_email` (`email`),
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table zhitiaoitem (
    `id` varchar(50) not null,
    `keywords` varchar(500) not null,
    `distance` bigint not null,
    `num` bigint not null,
    `lng` real ,
    `lat` real ,
    `alt` real ,
    `created_at` real not null,
    `owner` varchar(50) not null,
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;