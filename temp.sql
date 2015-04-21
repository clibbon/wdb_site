--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: warranty_db; Type: DATABASE; Schema: -; Owner: alex
--

CREATE DATABASE warranty_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_GB.UTF-8' LC_CTYPE = 'en_GB.UTF-8';


ALTER DATABASE warranty_db OWNER TO alex;

\connect warranty_db

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO clibbon;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO clibbon;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE auth_group_id_seq OWNED BY auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO clibbon;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO clibbon;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE auth_group_permissions_id_seq OWNED BY auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE auth_permission (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO clibbon;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO clibbon;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE auth_permission_id_seq OWNED BY auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone NOT NULL,
    is_superuser boolean NOT NULL,
    username character varying(30) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    email character varying(75) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO clibbon;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO clibbon;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO clibbon;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE auth_user_groups_id_seq OWNED BY auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO clibbon;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE auth_user_id_seq OWNED BY auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO clibbon;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO clibbon;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE auth_user_user_permissions_id_seq OWNED BY auth_user_user_permissions.id;


--
-- Name: customer; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE customer (
    cid integer NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    mob_number character varying(24) NOT NULL,
    region integer
);


ALTER TABLE public.customer OWNER TO clibbon;

--
-- Name: customer_cid_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE customer_cid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.customer_cid_seq OWNER TO clibbon;

--
-- Name: customer_cid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE customer_cid_seq OWNED BY customer.cid;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO clibbon;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO clibbon;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE django_admin_log_id_seq OWNED BY django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE django_content_type (
    id integer NOT NULL,
    name character varying(100) NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO clibbon;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO clibbon;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE django_content_type_id_seq OWNED BY django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO clibbon;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO clibbon;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE django_migrations_id_seq OWNED BY django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO clibbon;

--
-- Name: war_manager_importer; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE war_manager_importer (
    iid integer NOT NULL,
    identity character varying(30) NOT NULL,
    user_id_id integer NOT NULL
);


ALTER TABLE public.war_manager_importer OWNER TO clibbon;

--
-- Name: war_manager_importer_iid_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE war_manager_importer_iid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.war_manager_importer_iid_seq OWNER TO clibbon;

--
-- Name: war_manager_importer_iid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE war_manager_importer_iid_seq OWNED BY war_manager_importer.iid;


--
-- Name: war_manager_message; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE war_manager_message (
    id integer NOT NULL,
    msg_text character varying(511) NOT NULL,
    date_received date,
    mob_number character varying(24) NOT NULL,
    customer_id integer NOT NULL
);


ALTER TABLE public.war_manager_message OWNER TO clibbon;

--
-- Name: war_manager_message_id_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE war_manager_message_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.war_manager_message_id_seq OWNER TO clibbon;

--
-- Name: war_manager_message_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE war_manager_message_id_seq OWNED BY war_manager_message.id;


--
-- Name: war_manager_product; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE war_manager_product (
    pid integer NOT NULL,
    ser_num character varying(30) NOT NULL,
    model_id integer NOT NULL,
    "productImport_id" integer NOT NULL,
    warranty_id integer NOT NULL
);


ALTER TABLE public.war_manager_product OWNER TO clibbon;

--
-- Name: war_manager_product_pid_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE war_manager_product_pid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.war_manager_product_pid_seq OWNER TO clibbon;

--
-- Name: war_manager_product_pid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE war_manager_product_pid_seq OWNED BY war_manager_product.pid;


--
-- Name: war_manager_productimport; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE war_manager_productimport (
    pid integer NOT NULL,
    imp_date date,
    importer_id integer NOT NULL
);


ALTER TABLE public.war_manager_productimport OWNER TO clibbon;

--
-- Name: war_manager_productimport_pid_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE war_manager_productimport_pid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.war_manager_productimport_pid_seq OWNER TO clibbon;

--
-- Name: war_manager_productimport_pid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE war_manager_productimport_pid_seq OWNED BY war_manager_productimport.pid;


--
-- Name: war_manager_productmodel; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE war_manager_productmodel (
    mid integer NOT NULL,
    model character varying(20) NOT NULL,
    is_verified boolean NOT NULL,
    war_length integer NOT NULL
);


ALTER TABLE public.war_manager_productmodel OWNER TO clibbon;

--
-- Name: war_manager_productmodel_mid_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE war_manager_productmodel_mid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.war_manager_productmodel_mid_seq OWNER TO clibbon;

--
-- Name: war_manager_productmodel_mid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE war_manager_productmodel_mid_seq OWNED BY war_manager_productmodel.mid;


--
-- Name: war_manager_warranty; Type: TABLE; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE TABLE war_manager_warranty (
    wid integer NOT NULL,
    ser_num character varying(30) NOT NULL,
    reg_date date,
    exp_date date,
    customer_id integer NOT NULL
);


ALTER TABLE public.war_manager_warranty OWNER TO clibbon;

--
-- Name: war_manager_warranty_wid_seq; Type: SEQUENCE; Schema: public; Owner: clibbon
--

CREATE SEQUENCE war_manager_warranty_wid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.war_manager_warranty_wid_seq OWNER TO clibbon;

--
-- Name: war_manager_warranty_wid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: clibbon
--

ALTER SEQUENCE war_manager_warranty_wid_seq OWNED BY war_manager_warranty.wid;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY auth_group ALTER COLUMN id SET DEFAULT nextval('auth_group_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('auth_group_permissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY auth_permission ALTER COLUMN id SET DEFAULT nextval('auth_permission_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY auth_user ALTER COLUMN id SET DEFAULT nextval('auth_user_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY auth_user_groups ALTER COLUMN id SET DEFAULT nextval('auth_user_groups_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('auth_user_user_permissions_id_seq'::regclass);


--
-- Name: cid; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY customer ALTER COLUMN cid SET DEFAULT nextval('customer_cid_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY django_admin_log ALTER COLUMN id SET DEFAULT nextval('django_admin_log_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY django_content_type ALTER COLUMN id SET DEFAULT nextval('django_content_type_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY django_migrations ALTER COLUMN id SET DEFAULT nextval('django_migrations_id_seq'::regclass);


--
-- Name: iid; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY war_manager_importer ALTER COLUMN iid SET DEFAULT nextval('war_manager_importer_iid_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY war_manager_message ALTER COLUMN id SET DEFAULT nextval('war_manager_message_id_seq'::regclass);


--
-- Name: pid; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY war_manager_product ALTER COLUMN pid SET DEFAULT nextval('war_manager_product_pid_seq'::regclass);


--
-- Name: pid; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY war_manager_productimport ALTER COLUMN pid SET DEFAULT nextval('war_manager_productimport_pid_seq'::regclass);


--
-- Name: mid; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY war_manager_productmodel ALTER COLUMN mid SET DEFAULT nextval('war_manager_productmodel_mid_seq'::regclass);


--
-- Name: wid; Type: DEFAULT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY war_manager_warranty ALTER COLUMN wid SET DEFAULT nextval('war_manager_warranty_wid_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add permission	2	add_permission
5	Can change permission	2	change_permission
6	Can delete permission	2	delete_permission
7	Can add group	3	add_group
8	Can change group	3	change_group
9	Can delete group	3	delete_group
10	Can add user	4	add_user
11	Can change user	4	change_user
12	Can delete user	4	delete_user
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add customer	7	add_customer
20	Can change customer	7	change_customer
21	Can delete customer	7	delete_customer
22	Can add importer	8	add_importer
23	Can change importer	8	change_importer
24	Can delete importer	8	delete_importer
25	Can add product model	9	add_productmodel
26	Can change product model	9	change_productmodel
27	Can delete product model	9	delete_productmodel
28	Can add product import	10	add_productimport
29	Can change product import	10	change_productimport
30	Can delete product import	10	delete_productimport
31	Can add warranty	11	add_warranty
32	Can change warranty	11	change_warranty
33	Can delete warranty	11	delete_warranty
34	Can add product	12	add_product
35	Can change product	12	change_product
36	Can delete product	12	delete_product
37	Can add message	13	add_message
38	Can change message	13	change_message
39	Can delete message	13	delete_message
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('auth_permission_id_seq', 39, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$15000$QGpkjdv0M2Ax$9lePSqQHlYRufG+qg3znCTNWXLDXoqcIFt+rEc4KcJA=	2015-04-21 12:28:18.196615+01	t	clibbon			alex.clibbon@gmail.com	t	t	2015-04-21 12:28:18.196615+01
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('auth_user_id_seq', 1, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: customer; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY customer (cid, first_name, last_name, mob_number, region) FROM stdin;
\.


--
-- Name: customer_cid_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('customer_cid_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('django_admin_log_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY django_content_type (id, name, app_label, model) FROM stdin;
1	log entry	admin	logentry
2	permission	auth	permission
3	group	auth	group
4	user	auth	user
5	content type	contenttypes	contenttype
6	session	sessions	session
7	customer	war_manager	customer
8	importer	war_manager	importer
9	product model	war_manager	productmodel
10	product import	war_manager	productimport
11	warranty	war_manager	warranty
12	product	war_manager	product
13	message	war_manager	message
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('django_content_type_id_seq', 13, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2015-04-21 12:27:57.147078+01
2	auth	0001_initial	2015-04-21 12:27:57.233886+01
3	admin	0001_initial	2015-04-21 12:27:57.340972+01
4	sessions	0001_initial	2015-04-21 12:27:57.355444+01
5	war_manager	0001_initial	2015-04-21 13:27:00.030222+01
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('django_migrations_id_seq', 5, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: war_manager_importer; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY war_manager_importer (iid, identity, user_id_id) FROM stdin;
\.


--
-- Name: war_manager_importer_iid_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('war_manager_importer_iid_seq', 1, false);


--
-- Data for Name: war_manager_message; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY war_manager_message (id, msg_text, date_received, mob_number, customer_id) FROM stdin;
\.


--
-- Name: war_manager_message_id_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('war_manager_message_id_seq', 1, false);


--
-- Data for Name: war_manager_product; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY war_manager_product (pid, ser_num, model_id, "productImport_id", warranty_id) FROM stdin;
\.


--
-- Name: war_manager_product_pid_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('war_manager_product_pid_seq', 1, false);


--
-- Data for Name: war_manager_productimport; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY war_manager_productimport (pid, imp_date, importer_id) FROM stdin;
\.


--
-- Name: war_manager_productimport_pid_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('war_manager_productimport_pid_seq', 1, false);


--
-- Data for Name: war_manager_productmodel; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY war_manager_productmodel (mid, model, is_verified, war_length) FROM stdin;
\.


--
-- Name: war_manager_productmodel_mid_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('war_manager_productmodel_mid_seq', 1, false);


--
-- Data for Name: war_manager_warranty; Type: TABLE DATA; Schema: public; Owner: clibbon
--

COPY war_manager_warranty (wid, ser_num, reg_date, exp_date, customer_id) FROM stdin;
\.


--
-- Name: war_manager_warranty_wid_seq; Type: SEQUENCE SET; Schema: public; Owner: clibbon
--

SELECT pg_catalog.setval('war_manager_warranty_wid_seq', 1, false);


--
-- Name: auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions_group_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_key UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission_content_type_id_codename_key; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_key UNIQUE (content_type_id, codename);


--
-- Name: auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups_user_id_group_id_key; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_key UNIQUE (user_id, group_id);


--
-- Name: auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions_user_id_permission_id_key; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_key UNIQUE (user_id, permission_id);


--
-- Name: auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: customer_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (cid);


--
-- Name: django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type_app_label_45f3b1d93ec8c61c_uniq; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_app_label_45f3b1d93ec8c61c_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: war_manager_importer_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY war_manager_importer
    ADD CONSTRAINT war_manager_importer_pkey PRIMARY KEY (iid);


--
-- Name: war_manager_message_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY war_manager_message
    ADD CONSTRAINT war_manager_message_pkey PRIMARY KEY (id);


--
-- Name: war_manager_product_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY war_manager_product
    ADD CONSTRAINT war_manager_product_pkey PRIMARY KEY (pid);


--
-- Name: war_manager_productimport_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY war_manager_productimport
    ADD CONSTRAINT war_manager_productimport_pkey PRIMARY KEY (pid);


--
-- Name: war_manager_productmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY war_manager_productmodel
    ADD CONSTRAINT war_manager_productmodel_pkey PRIMARY KEY (mid);


--
-- Name: war_manager_warranty_pkey; Type: CONSTRAINT; Schema: public; Owner: clibbon; Tablespace: 
--

ALTER TABLE ONLY war_manager_warranty
    ADD CONSTRAINT war_manager_warranty_pkey PRIMARY KEY (wid);


--
-- Name: auth_group_name_253ae2a6331666e8_like; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX auth_group_name_253ae2a6331666e8_like ON auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_0e939a4f; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX auth_group_permissions_0e939a4f ON auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_8373b171; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX auth_group_permissions_8373b171 ON auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_417f1b1c; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX auth_permission_417f1b1c ON auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_0e939a4f; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX auth_user_groups_0e939a4f ON auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_e8701ad4; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX auth_user_groups_e8701ad4 ON auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_8373b171; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_8373b171 ON auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_e8701ad4; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX auth_user_user_permissions_e8701ad4 ON auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_51b3b110094b8aae_like; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX auth_user_username_51b3b110094b8aae_like ON auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_417f1b1c; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX django_admin_log_417f1b1c ON django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_e8701ad4; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX django_admin_log_e8701ad4 ON django_admin_log USING btree (user_id);


--
-- Name: django_session_de54fa62; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX django_session_de54fa62 ON django_session USING btree (expire_date);


--
-- Name: django_session_session_key_461cfeaa630ca218_like; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX django_session_session_key_461cfeaa630ca218_like ON django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: war_manager_importer_18624dd3; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX war_manager_importer_18624dd3 ON war_manager_importer USING btree (user_id_id);


--
-- Name: war_manager_message_cb24373b; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX war_manager_message_cb24373b ON war_manager_message USING btree (customer_id);


--
-- Name: war_manager_product_1ca1f9bd; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX war_manager_product_1ca1f9bd ON war_manager_product USING btree ("productImport_id");


--
-- Name: war_manager_product_477cbf8a; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX war_manager_product_477cbf8a ON war_manager_product USING btree (model_id);


--
-- Name: war_manager_product_6fbdb817; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX war_manager_product_6fbdb817 ON war_manager_product USING btree (warranty_id);


--
-- Name: war_manager_productimport_bc9dcfc6; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX war_manager_productimport_bc9dcfc6 ON war_manager_productimport USING btree (importer_id);


--
-- Name: war_manager_warranty_cb24373b; Type: INDEX; Schema: public; Owner: clibbon; Tablespace: 
--

CREATE INDEX war_manager_warranty_cb24373b ON war_manager_warranty USING btree (customer_id);


--
-- Name: auth_content_type_id_508cf46651277a81_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY auth_permission
    ADD CONSTRAINT auth_content_type_id_508cf46651277a81_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_group_id_689710a9a73b7457_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY auth_group_permissions
    ADD CONSTRAINT auth_group_permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user__permission_id_384b62483d7071f0_fk_auth_permission_id FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permiss_user_id_7f0938558328534a_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: c4418d112d597f25a39120281ac6e960; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY war_manager_product
    ADD CONSTRAINT c4418d112d597f25a39120281ac6e960 FOREIGN KEY ("productImport_id") REFERENCES war_manager_productimport(pid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: djan_content_type_id_697914295151027a_fk_django_content_type_id; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT djan_content_type_id_697914295151027a_fk_django_content_type_id FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: war_m_model_id_455f3b59f7ad64b9_fk_war_manager_productmodel_mid; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY war_manager_product
    ADD CONSTRAINT war_m_model_id_455f3b59f7ad64b9_fk_war_manager_productmodel_mid FOREIGN KEY (model_id) REFERENCES war_manager_productmodel(mid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: war_ma_importer_id_775ad28abe99c104_fk_war_manager_importer_iid; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY war_manager_productimport
    ADD CONSTRAINT war_ma_importer_id_775ad28abe99c104_fk_war_manager_importer_iid FOREIGN KEY (importer_id) REFERENCES war_manager_importer(iid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: war_ma_warranty_id_1708267be7ccf6a9_fk_war_manager_warranty_wid; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY war_manager_product
    ADD CONSTRAINT war_ma_warranty_id_1708267be7ccf6a9_fk_war_manager_warranty_wid FOREIGN KEY (warranty_id) REFERENCES war_manager_warranty(wid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: war_manager_importe_user_id_id_578a7b6691fe0b11_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY war_manager_importer
    ADD CONSTRAINT war_manager_importe_user_id_id_578a7b6691fe0b11_fk_auth_user_id FOREIGN KEY (user_id_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: war_manager_messag_customer_id_7bbf63b53390c2e7_fk_customer_cid; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY war_manager_message
    ADD CONSTRAINT war_manager_messag_customer_id_7bbf63b53390c2e7_fk_customer_cid FOREIGN KEY (customer_id) REFERENCES customer(cid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: war_manager_warran_customer_id_79dfabafd11e2769_fk_customer_cid; Type: FK CONSTRAINT; Schema: public; Owner: clibbon
--

ALTER TABLE ONLY war_manager_warranty
    ADD CONSTRAINT war_manager_warran_customer_id_79dfabafd11e2769_fk_customer_cid FOREIGN KEY (customer_id) REFERENCES customer(cid) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

