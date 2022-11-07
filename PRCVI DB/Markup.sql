-- Table: public.Markup

-- DROP TABLE IF EXISTS public."Markup";

CREATE TABLE IF NOT EXISTS public."Markup"
(
    markup_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    image_id integer NOT NULL,
    image character varying(250) COLLATE pg_catalog."default" NOT NULL,
    type character varying(50) COLLATE pg_catalog."default",
    CONSTRAINT "Markup_pkey" PRIMARY KEY (markup_id),
    CONSTRAINT fkey_1 FOREIGN KEY (image_id)
        REFERENCES public."Sources" (image_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Markup"
    OWNER to postgres;