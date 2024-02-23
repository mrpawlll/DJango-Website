--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1 (Debian 16.1-1.pgdg120+1)
-- Dumped by pg_dump version 16.1 (Debian 16.1-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id bigint NOT NULL,
    name text
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id bigint,
    permission_id bigint
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id bigint NOT NULL,
    content_type_id bigint,
    codename text,
    name text
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id bigint NOT NULL,
    password text,
    last_login timestamp with time zone,
    is_superuser boolean,
    username text,
    last_name text,
    email text,
    is_staff boolean,
    is_active boolean,
    date_joined timestamp with time zone,
    first_name text
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id bigint,
    group_id bigint
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id bigint,
    permission_id bigint
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: deliveryorder_deliveryorderform; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.deliveryorder_deliveryorderform (
    deliveryorderid bigint NOT NULL,
    vendorname text,
    vendoraddress text,
    recipientname text,
    recipientphone text,
    recipientaddress text,
    deliveryorderstatus bigint,
    deliveryorderdate timestamp with time zone,
    itemid bigint,
    itemquantity bigint,
    itemdescription text,
    itemprice numeric,
    courierstatus bigint,
    invoicetotal numeric,
    invoicestatus bigint,
    invoicecreated boolean
);


ALTER TABLE public.deliveryorder_deliveryorderform OWNER TO postgres;

--
-- Name: deliveryorder_deliveryorderform_deliveryorderid_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.deliveryorder_deliveryorderform_deliveryorderid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.deliveryorder_deliveryorderform_deliveryorderid_seq OWNER TO postgres;

--
-- Name: deliveryorder_deliveryorderform_deliveryorderid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.deliveryorder_deliveryorderform_deliveryorderid_seq OWNED BY public.deliveryorder_deliveryorderform.deliveryorderid;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id bigint NOT NULL,
    object_id text,
    object_repr text,
    action_flag smallint,
    change_message text,
    content_type_id bigint,
    user_id bigint,
    action_time timestamp with time zone
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id bigint NOT NULL,
    app_label text,
    model text
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app text,
    name text,
    applied timestamp with time zone
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key text NOT NULL,
    session_data text,
    expire_date timestamp with time zone
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: deliveryorder_deliveryorderform deliveryorderid; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deliveryorder_deliveryorderform ALTER COLUMN deliveryorderid SET DEFAULT nextval('public.deliveryorder_deliveryorderform_deliveryorderid_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
1	Manager
2	Salesman
3	Courier
4	Finance
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	8
2	1	6
3	2	8
4	2	5
5	3	8
6	3	6
7	4	8
8	4	6
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, content_type_id, codename, name) FROM stdin;
1	1	add_item	Can add item
2	1	change_item	Can change item
3	1	delete_item	Can delete item
4	1	view_item	Can view item
5	2	add_deliveryorderform	Can add delivery order form
6	2	change_deliveryorderform	Can change delivery order form
7	2	delete_deliveryorderform	Can delete delivery order form
8	2	view_deliveryorderform	Can view delivery order form
9	3	add_logentry	Can add log entry
10	3	change_logentry	Can change log entry
11	3	delete_logentry	Can delete log entry
12	3	view_logentry	Can view log entry
13	4	add_permission	Can add permission
14	4	change_permission	Can change permission
15	4	delete_permission	Can delete permission
16	4	view_permission	Can view permission
17	5	add_group	Can add group
18	5	change_group	Can change group
19	5	delete_group	Can delete group
20	5	view_group	Can view group
21	6	add_user	Can add user
22	6	change_user	Can change user
23	6	delete_user	Can delete user
24	6	view_user	Can view user
25	7	add_contenttype	Can add content type
26	7	change_contenttype	Can change content type
27	7	delete_contenttype	Can delete content type
28	7	view_contenttype	Can view content type
29	8	add_session	Can add session
30	8	change_session	Can change session
31	8	delete_session	Can delete session
32	8	view_session	Can view session
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, last_name, email, is_staff, is_active, date_joined, first_name) FROM stdin;
1	pbkdf2_sha256$720000$UhaCZNxsakni2bZVxyKtNC$XgDm6MGXZ/j3OlLg/QOVEEu8Nm+S7l2zZSNi9DMSkpo=	2023-12-27 01:16:54.481645+00	t	admin		admin@admin.com	t	t	2023-01-25 15:00:04.648929+00	
2	pbkdf2_sha256$720000$2IZFaK29L82QR7H5DhQjR4$2nbWkD0sKw4V/srO9JpcGG/8YvbVhTdYRFNSiom57Ic=	2024-02-02 12:52:28.476048+00	f	manager			f	t	2023-01-25 15:03:26+00	
3	pbkdf2_sha256$720000$InBnbb5ZfpK9vuRvtjHy13$04B7rmS0fEMZsVBAi+cPSzM23FerwQi338bW7/JZqN4=	2023-12-22 14:46:05.012603+00	f	salesman			f	t	2023-01-25 15:03:39+00	
4	pbkdf2_sha256$720000$IiR3QMj2w2SBgXfJ0qLofn$/o8/P+gqKdRUZA3RB+/trDpB2qYPdqpowG/U9IUjhag=	2023-12-22 14:48:25.635125+00	f	financeoffice			f	t	2023-01-25 15:06:17+00	
5	pbkdf2_sha256$720000$RtNvniNHgChqTs43pPVV2Q$Gy0uahrKhl3Iexkk3uZ6rPSXpI9g21/4PDL9fbJ32xE=	2023-12-22 14:48:07.168662+00	f	courier			f	t	2023-01-25 18:57:12+00	
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
1	2	1
2	3	2
3	5	3
4	4	4
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: deliveryorder_deliveryorderform; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.deliveryorder_deliveryorderform (deliveryorderid, vendorname, vendoraddress, recipientname, recipientphone, recipientaddress, deliveryorderstatus, deliveryorderdate, itemid, itemquantity, itemdescription, itemprice, courierstatus, invoicetotal, invoicestatus, invoicecreated) FROM stdin;
27	VENDORNAME	CYBERJAYA	TEST3	+601156309196	TEST3	3	2023-01-26 03:17:26+00	4678	2	fish	50	3	100	3	t
29	VENDORNAME	CYBERJAYA	TEST01	+601111111111	TEST01	3	2023-12-22 14:46:06+00	5	2	TEST	1.5	3	3	3	t
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, object_id, object_repr, action_flag, change_message, content_type_id, user_id, action_time) FROM stdin;
1	1	0001	1	[{"added": {}}]	1	1	2023-01-25 15:00:26.557947+00
2	2	0002	1	[{"added": {}}]	1	1	2023-01-25 15:00:37.880559+00
3	3	0003	1	[{"added": {}}]	1	1	2023-01-25 15:00:45.899393+00
4	1	Manager	1	[{"added": {}}]	5	1	2023-01-25 15:07:34.034602+00
5	1	ID : 1 - TESTADMIN	1	[{"added": {}}]	2	1	2023-01-25 15:16:03.343119+00
6	2	Salesman	1	[{"added": {}}]	5	1	2023-01-25 15:18:06.573618+00
7	3	Courier	1	[{"added": {}}]	5	1	2023-01-25 15:18:14.123028+00
8	2	manager	2	[{"changed": {"fields": ["Groups"]}}]	6	1	2023-01-25 15:18:59.064551+00
9	3	salesman	2	[{"changed": {"fields": ["Groups"]}}]	6	1	2023-01-25 15:19:06.245508+00
10	7	ID : 7 - RECIPIENTNAME	2	[{"changed": {"fields": ["DeliveryOrderStatus"]}}]	2	1	2023-01-25 17:00:03.645629+00
11	3	Courier	2	[{"changed": {"fields": ["Permissions"]}}]	5	1	2023-01-25 18:57:54.679958+00
12	5	courier	2	[{"changed": {"fields": ["Groups"]}}]	6	1	2023-01-25 18:58:03.420645+00
13	4	Finance	1	[{"added": {}}]	5	1	2023-01-25 22:11:17.076138+00
14	4	financeoffice	2	[{"changed": {"fields": ["Groups"]}}]	6	1	2023-01-25 22:11:25.818201+00
15	28	ID : 28 - TEST5	3		2	1	2023-12-21 11:16:27.935226+00
16	25	ID : 25 - TEST1	3		2	1	2023-12-21 11:16:48.835064+00
17	26	ID : 26 - TEST2	3		2	1	2023-12-21 11:16:57.971921+00
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	deliveryorder	item
2	deliveryorder	deliveryorderform
3	admin	logentry
4	auth	permission
5	auth	group
6	auth	user
7	contenttypes	contenttype
8	sessions	session
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2023-01-25 14:58:44.556219+00
2	auth	0001_initial	2023-01-25 14:58:44.569221+00
3	admin	0001_initial	2023-01-25 14:58:44.577281+00
4	admin	0002_logentry_remove_auto_add	2023-01-25 14:58:44.586227+00
5	admin	0003_logentry_add_action_flag_choices	2023-01-25 14:58:44.591227+00
6	contenttypes	0002_remove_content_type_name	2023-01-25 14:58:44.604848+00
7	auth	0002_alter_permission_name_max_length	2023-01-25 14:58:44.613852+00
8	auth	0003_alter_user_email_max_length	2023-01-25 14:58:44.621854+00
9	auth	0004_alter_user_username_opts	2023-01-25 14:58:44.627778+00
10	auth	0005_alter_user_last_login_null	2023-01-25 14:58:44.63578+00
11	auth	0006_require_contenttypes_0002	2023-01-25 14:58:44.638139+00
12	auth	0007_alter_validators_add_error_messages	2023-01-25 14:58:44.644141+00
13	auth	0008_alter_user_username_max_length	2023-01-25 14:58:44.652143+00
14	auth	0009_alter_user_last_name_max_length	2023-01-25 14:58:44.659714+00
15	auth	0010_alter_group_name_max_length	2023-01-25 14:58:44.667716+00
16	auth	0011_update_proxy_permissions	2023-01-25 14:58:44.673717+00
17	auth	0012_alter_user_first_name_max_length	2023-01-25 14:58:44.681642+00
18	deliveryorder	0001_initial	2023-01-25 14:58:44.686644+00
19	deliveryorder	0002_item_itemprice	2023-01-25 14:58:44.691644+00
20	deliveryorder	0003_rename_deliveryorder_deliveryorderform	2023-01-25 14:58:44.701647+00
21	deliveryorder	0004_deliveryorderformitemlist	2023-01-25 14:58:44.708648+00
22	deliveryorder	0005_rename_deliveryorderformitemlist_tablelist	2023-01-25 14:58:44.718651+00
23	deliveryorder	0006_deliveryorderform_deliveryorderdate	2023-01-25 14:58:44.724652+00
24	deliveryorder	0007_alter_deliveryorderform_deliveryorderdate_and_more	2023-01-25 14:58:44.733655+00
25	deliveryorder	0008_alter_deliveryorderform_deliveryorderdate_and_more	2023-01-25 14:58:44.743062+00
26	deliveryorder	0009_deliveryorderform_itemid_and_more	2023-01-25 14:58:44.753064+00
27	deliveryorder	0010_alter_deliveryorderform_itemid	2023-01-25 14:58:44.761066+00
28	sessions	0001_initial	2023-01-25 14:58:44.767068+00
29	deliveryorder	0011_alter_deliveryorderform_itemid	2023-01-25 14:58:56.919376+00
30	deliveryorder	0012_deliveryorderform_itemdescription_and_more	2023-01-25 15:11:43.690676+00
31	deliveryorder	0013_alter_deliveryorderform_recipientaddress_and_more	2023-01-25 16:01:31.210542+00
32	deliveryorder	0014_deliveryorderform_courierstatus_and_more	2023-01-25 18:52:24.363112+00
33	deliveryorder	0015_alter_deliveryorderform_courierstatus	2023-01-25 21:16:57.916138+00
34	deliveryorder	0016_deliveryorderform_invoicestatus	2023-01-25 22:14:51.773678+00
35	deliveryorder	0017_remove_deliveryorderform_invoicestatus	2023-01-25 22:59:05.071329+00
36	deliveryorder	0018_deliveryorderform_invoicestatus	2023-01-25 23:00:51.086332+00
37	deliveryorder	0019_deliveryorderform_invoicecreated	2023-01-25 23:03:43.425395+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
lghgydysljfa0phz0lllnzfx0q4hfe44	.eJxVjEsOwjAMBe-SNYrS2GmBJXvOEDm2IQWUSP2sEHenkbqA7cy89zaR1iXHddYpjmLOxpvDL0vETy1NyIPKvVquZZnGZFtidzvbaxV9Xfb27yDTnLc1OgiIckOSpCrUd6ycAtGQKOCJYeAeXGDoELwDdxy2hjwqNyhgPl__sjg5:1rGcV3:hkKvWTeIJDvYBarkRmmItKm27Zz426OtPZIZ5eSDkss	2024-01-05 10:11:25.147712+00
b4xlv51yukb06maxizyo6qlfebk7n0mj	.eJxVjEEOwiAQRe_C2pAWCgwu3fcMZGAGqRqalHZlvLtt0oVu_3vvv0XAbS1ha7yEicRVKHH53SKmJ9cD0APrfZZprusyRXko8qRNjjPx63a6fwcFW9nrIRqtXc926H2CpDgDatLeWkO2i6yyjQnAekUeILouGyY0u-eSypjF5wvaHzhT:1rGpZC:Q6KhGBPfPZhh5JrYm3KhKvXifuzJ7NpeaPPlhyxjaBg	2024-01-06 00:08:34.204731+00
sbui6n5bslvmmmuprqbjkx9c1izu8om2	.eJxVjEEOwiAQRe_C2pAWCgwu3fcMZGAGqRqalHZlvLtt0oVu_3vvv0XAbS1ha7yEicRVKHH53SKmJ9cD0APrfZZprusyRXko8qRNjjPx63a6fwcFW9nrIRqtXc926H2CpDgDatLeWkO2i6yyjQnAekUeILouGyY0u-eSypjF5wvaHzhT:1rHOH2:SGkv9fPiFJPuyHhxzKCixO175UklI_wqjfNIDU9OoSI	2024-01-07 13:12:08.657822+00
9k4b3pufjs24udouky10n7b3pycwwysb	.eJxVjMEOwiAQRP-FsyHAFko9eu83kF0WpGpoUtqT8d9tkx70OPPezFsE3NYStpaWMLG4Ci0uvx1hfKZ6AH5gvc8yznVdJpKHIk_a5Dhzet1O9--gYCv72unBZ6ZOeTLJQE4qMujEVrkOwTirSQFmtWfvgACBUCH1A8feWtDi8wXa8Dd-:1rIIXV:EuZVALqlnI8A5GxFK09aX0-wZdUM-VHil8FP0uKGdHY	2024-01-10 01:16:53.673672+00
4ttedub05imyrvmiblfza8mnrsu84m8x	.eJxVjMEOwiAQRP-FsyHAFko9eu83kF0WpGpoUtqT8d9tkx70OPPezFsE3NYStpaWMLG4Ci0uvx1hfKZ6AH5gvc8yznVdJpKHIk_a5Dhzet1O9--gYCv72unBZ6ZOeTLJQE4qMujEVrkOwTirSQFmtWfvgACBUCH1A8feWtDi8wXa8Dd-:1rIIXW:pSl0mnxc-U9gIfpZIlgcMW3zdk3E69PK5ybzYvpOcEw	2024-01-10 01:16:54.483559+00
gwctbfk0drs9gb942s3bpb0ji8cxmcvr	.eJxVjEEOwiAQRe_C2pAWCgwu3fcMZGAGqRqalHZlvLtt0oVu_3vvv0XAbS1ha7yEicRVKHH53SKmJ9cD0APrfZZprusyRXko8qRNjjPx63a6fwcFW9nrIRqtXc926H2CpDgDatLeWkO2i6yyjQnAekUeILouGyY0u-eSypjF5wvaHzhT:1rVt1w:svJKNMgaAxv82M5B4eOly6T2pI85paEQAeUhkrztBks	2024-02-16 12:52:28.480048+00
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 4, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 8, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 32, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 4, true);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 5, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, true);


--
-- Name: deliveryorder_deliveryorderform_deliveryorderid_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.deliveryorder_deliveryorderform_deliveryorderid_seq', 29, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 17, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 8, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 37, true);


--
-- Name: django_migrations idx_16391_django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT idx_16391_django_migrations_pkey PRIMARY KEY (id);


--
-- Name: auth_group_permissions idx_16398_auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT idx_16398_auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups idx_16403_auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT idx_16403_auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions idx_16408_auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT idx_16408_auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log idx_16413_django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT idx_16413_django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type idx_16420_django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT idx_16420_django_content_type_pkey PRIMARY KEY (id);


--
-- Name: auth_permission idx_16427_auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT idx_16427_auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_group idx_16434_auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT idx_16434_auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_user idx_16441_auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT idx_16441_auth_user_pkey PRIMARY KEY (id);


--
-- Name: django_session idx_16447_sqlite_autoindex_django_session_1; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT idx_16447_sqlite_autoindex_django_session_1 PRIMARY KEY (session_key);


--
-- Name: deliveryorder_deliveryorderform idx_16453_deliveryorder_deliveryorderform_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.deliveryorder_deliveryorderform
    ADD CONSTRAINT idx_16453_deliveryorder_deliveryorderform_pkey PRIMARY KEY (deliveryorderid);


--
-- Name: idx_16398_auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16398_auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: idx_16398_auth_group_permissions_group_id_permission_id_0cd325b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16398_auth_group_permissions_group_id_permission_id_0cd325b ON public.auth_group_permissions USING btree (group_id, permission_id);


--
-- Name: idx_16398_auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16398_auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: idx_16403_auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16403_auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: idx_16403_auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16403_auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: idx_16403_auth_user_groups_user_id_group_id_94350c0c_uniq; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16403_auth_user_groups_user_id_group_id_94350c0c_uniq ON public.auth_user_groups USING btree (user_id, group_id);


--
-- Name: idx_16408_auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16408_auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: idx_16408_auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16408_auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: idx_16408_auth_user_user_permissions_user_id_permission_id_14a6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16408_auth_user_user_permissions_user_id_permission_id_14a6 ON public.auth_user_user_permissions USING btree (user_id, permission_id);


--
-- Name: idx_16413_django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16413_django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: idx_16413_django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16413_django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: idx_16420_django_content_type_app_label_model_76bd3d3b_uniq; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16420_django_content_type_app_label_model_76bd3d3b_uniq ON public.django_content_type USING btree (app_label, model);


--
-- Name: idx_16427_auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16427_auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: idx_16427_auth_permission_content_type_id_codename_01ab375a_uni; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16427_auth_permission_content_type_id_codename_01ab375a_uni ON public.auth_permission USING btree (content_type_id, codename);


--
-- Name: idx_16434_sqlite_autoindex_auth_group_1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16434_sqlite_autoindex_auth_group_1 ON public.auth_group USING btree (name);


--
-- Name: idx_16441_sqlite_autoindex_auth_user_1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX idx_16441_sqlite_autoindex_auth_user_1 ON public.auth_user USING btree (username);


--
-- Name: idx_16447_django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX idx_16447_django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.auth_group(id);


--
-- Name: auth_group_permissions auth_group_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id);


--
-- Name: auth_permission auth_permission_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id);


--
-- Name: auth_user_groups auth_user_groups_group_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_fkey FOREIGN KEY (group_id) REFERENCES public.auth_group(id);


--
-- Name: auth_user_groups auth_user_groups_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_permission_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_permission_id_fkey FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- Name: django_admin_log django_admin_log_content_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_fkey FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id);


--
-- Name: django_admin_log django_admin_log_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.auth_user(id);


--
-- PostgreSQL database dump complete
--

