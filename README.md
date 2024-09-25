В 8 пункте ТЗ есть формулировка:
•	В работе (средний показатель за отчётный период), шт
Расчёт показателя «в работе» осуществляется по следующему принципу, это сумма скважин, работающих определенное время, отличное от нуля, за сутки на проекте/ах.
Есть ли данные по отдельной скважине? 
Если нет, то откуда брать данные?


--------------------

Добавить about_wells

CREATE TABLE about_wells (
	about_wells_guid varchar(40) NOT NULL,
	c_date date NOT NULL,
	period_type_guid varchar(40) NULL,
	asset_guid varchar(40) NULL,
	active_wells int4 NULL,
	info_type_guid varchar(40) NULL,
	CONSTRAINT about_wells_pkey PRIMARY KEY (about_wells_guid)
);


-- public.about_wells внешние включи

ALTER TABLE public.about_wells ADD CONSTRAINT fk_asset_guid FOREIGN KEY (asset_guid) REFERENCES assets(asset_guid);
ALTER TABLE public.about_wells ADD CONSTRAINT fk_info_type_guid FOREIGN KEY (info_type_guid) REFERENCES infos(info_type_guid);
ALTER TABLE public.about_wells ADD CONSTRAINT fk_period_type_guid FOREIGN KEY (period_type_guid) REFERENCES periods(period_type_guid);




Удалить из wells status?


Переписать всю концепцию скважин

то есть:
1) Скважины (гуид, название, актив, всего скважин?)
2) Обновление по активу [тотал] (гуид операции, гуид актива, всего скважин, активных)
3) Обновление по скважинам [глобал] (гуид операции, гуид скважины, дата операции, период, объем, ЕИ, время работы)




Добавить инфу про устье?



Сделать sql запрос на вывод минимальных и максимальных данных за период. 
Учесть - период (столбец), ЕИ, флюид, актив	
