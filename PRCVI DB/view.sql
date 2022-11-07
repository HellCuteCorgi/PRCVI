-- View: public.price_view1

-- DROP VIEW public.price_view1;

CREATE OR REPLACE VIEW public.price_view1
 AS
 SELECT m.markup_id,
    m.image,
    s.image AS image_sources,
    m.type,
    s.region,
    s.date
   FROM "Markup" m
     JOIN "Sources" s ON s.image_id = m.image_id;
d
ALTER TABLE public.price_view1
    OWNER TO postgres;

