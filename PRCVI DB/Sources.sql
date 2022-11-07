-- Table: public.Sources

-- DROP TABLE IF EXISTS public."Sources";

CREATE TABLE IF NOT EXISTS public."Sources"
(
    image_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    region character varying(100) COLLATE pg_catalog."default" NOT NULL,
    date time without time zone NOT NULL,
    image character varying(250) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Sources_pkey" PRIMARY KEY (image_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Sources"
    OWNER to postgres;