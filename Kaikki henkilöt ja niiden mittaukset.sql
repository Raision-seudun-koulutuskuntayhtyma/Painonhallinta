SELECT henkilo.henkilo_id, henkilo.sukunimi, henkilo.etunimi, mittaus.mittaus_id, mittaus.pituus, mittaus.paino
FROM henkilo LEFT OUTER JOIN mittaus ON henkilo.henkilo_id = mittaus.henkilo_id
