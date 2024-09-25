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


---------
Добавить Store - Flask или Dash
- XlsxWriter                3.0.9
- SQLAlchemy                2.0.29
- Flask                     2.2.2
Flask-APScheduler         1.12.4
Flask-Caching             2.0.1
Flask-Compress            1.12
Flask-Cors                3.0.10
Flask-Login               0.6.3
Flask-SeaSurf             1.1.1
Flask-Session             0.4.0
Flask-SQLAlchemy          3.0.3
dash                      2.15.0
dash-ag-grid              31.0.1
dash-auth                 1.4.1
dash-bootstrap-components 1.2.1
dash-core-components      2.0.0
dash-html-components      2.0.0
dash_mantine_components   0.12.1
dash-pivottable           0.0.2
dash-table                5.0.0
altgraph                  0.17.3
pandas                    1.4.4
numpy                     1.23.3
plotly                    5.22.0
plotly-geo                1.0.0
plotly-resampler          0.10.0
matplotlib                3.7.0
