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

-------------------------


CREATE table if not exists commercial_data (
    id SERIAL NOT NULL,
    h_date DATE NOT NULL,
    period_type VARCHAR(50) NOT NULL,
    project_id INT NOT NULL,
    value numeric(23, 12), 
    unit_id INT,
    hydrocarbon_id INT,
    comment TEXT,
    old_project_id INT,
    old_value numeric(23, 12), 
    old_unit_id int,
    old_hydrocarbon_id int,
    old_comment TEXT,
    CONSTRAINT pk_commercial_data PRIMARY KEY (id),
    CONSTRAINT fk_commercial_data_project_id FOREIGN KEY (project_id) REFERENCES projects(project_id),
    CONSTRAINT fk_commercial_data_old_project_id FOREIGN KEY (old_project_id) REFERENCES projects(project_id),
    CONSTRAINT fk_commercial_data_unit_id FOREIGN KEY (unit_id) REFERENCES units(unit_id),
    CONSTRAINT fk_commercial_data_old_unit_id FOREIGN KEY (old_unit_id) REFERENCES units(unit_id),
    CONSTRAINT fk_commercial_data_hydrocarbon_id FOREIGN KEY (hydrocarbon_id) REFERENCES hydrocarbons(hydrocarbon_id),
    CONSTRAINT fk_commercial_data_old_hydrocarbon_id FOREIGN KEY (old_hydrocarbon_id) REFERENCES hydrocarbons(hydrocarbon_id)
);



CREATE table if not exists commercial_data_plan (
    id SERIAL NOT NULL,
    h_date DATE NOT NULL,
    period_type VARCHAR(50) NOT NULL,
    project_id INT NOT NULL,
    value numeric(23, 12), 
    unit_id INT,
    hydrocarbon_id INT,
    comment TEXT,
    old_project_id INT,
    old_value numeric(23, 12), 
    old_unit_id int,
    old_hydrocarbon_id int,
    old_comment TEXT,
    CONSTRAINT pk_commercial_data_plan PRIMARY KEY (id),
    CONSTRAINT fk_commercial_data_plan_project_id FOREIGN KEY (project_id) REFERENCES projects(project_id),
    CONSTRAINT fk_commercial_data_plan_old_project_id FOREIGN KEY (old_project_id) REFERENCES projects(project_id),
    CONSTRAINT fk_commercial_data_plan_unit_id FOREIGN KEY (unit_id) REFERENCES units(unit_id),
    CONSTRAINT fk_commercial_data_plan_old_unit_id FOREIGN KEY (old_unit_id) REFERENCES units(unit_id),
    CONSTRAINT fk_commercial_data_plan_hydrocarbon_id FOREIGN KEY (hydrocarbon_id) REFERENCES hydrocarbons(hydrocarbon_id),
    CONSTRAINT fk_commercial_data_plan_old_hydrocarbon_id FOREIGN KEY (old_hydrocarbon_id) REFERENCES hydrocarbons(hydrocarbon_id)
);



CREATE table if not exists commercial_data_nomination (
    id SERIAL NOT NULL,
    h_date DATE NOT NULL,
    period_type VARCHAR(50) NOT NULL,
    project_id INT NOT NULL,
    value numeric(23, 12), 
    unit_id INT,
    hydrocarbon_id INT,
    comment TEXT,
    old_project_id INT,
    old_value numeric(23, 12), 
    old_unit_id int,
    old_hydrocarbon_id int,
    old_comment TEXT,
    CONSTRAINT pk_commercial_data_nomination PRIMARY KEY (id),
    CONSTRAINT fk_commercial_data_nomination_project_id FOREIGN KEY (project_id) REFERENCES projects(project_id),
    CONSTRAINT fk_commercial_data_nomination_old_project_id FOREIGN KEY (old_project_id) REFERENCES projects(project_id),
    CONSTRAINT fk_commercial_data_nomination_unit_id FOREIGN KEY (unit_id) REFERENCES units(unit_id),
    CONSTRAINT fk_commercial_data_nomination_old_unit_id FOREIGN KEY (old_unit_id) REFERENCES units(unit_id),
    CONSTRAINT fk_commercial_data_nomination_hydrocarbon_id FOREIGN KEY (hydrocarbon_id) REFERENCES hydrocarbons(hydrocarbon_id),
    CONSTRAINT fk_commercial_data_nomination_old_hydrocarbon_id FOREIGN KEY (old_hydrocarbon_id) REFERENCES hydrocarbons(hydrocarbon_id)
);



CREATE TABLE if not exists consumption_data (
    id SERIAL,
    h_date DATE NOT NULL,
    period_type VARCHAR(50),
    burned_value numeric(23, 12),
    fuel_value numeric(23, 12),
    converted_value numeric(23, 12), 
    hydrocarbon_id INT,
    unit_id INT,
    project_id INT,     
    commentary text,
    CONSTRAINT pk_consumption_data PRIMARY KEY (id),
    CONSTRAINT fk_consumption_data_project_id FOREIGN KEY (project_id) REFERENCES projects(project_id),
    CONSTRAINT fk_consumption_data_hydrocarbon_id FOREIGN KEY (hydrocarbon_id) REFERENCES hydrocarbons(hydrocarbon_id),
    CONSTRAINT fk_consumption_data_unit_id FOREIGN KEY (unit_id) REFERENCES units(unit_id)
);


CREATE TABLE if not exists water_stats (
    id SERIAL,
    h_date DATE NOT NULL,
    period_type VARCHAR(50) NOT NULL,
    project_id INT NOT NULL,
    injection_value numeric(23, 12),
    util_value numeric(23, 12),
    unit_id INT,
    hydrocarbon_id INT,
    commentary TEXT,
    CONSTRAINT pk_water_stats PRIMARY KEY (id),
    CONSTRAINT fk_water_stats_project_id FOREIGN KEY (project_id) REFERENCES projects(project_id),
    CONSTRAINT fk_water_stats_hydrocarbon_id FOREIGN KEY (hydrocarbon_id) REFERENCES hydrocarbons(hydrocarbon_id),
    CONSTRAINT fk_water_stats_unit_id FOREIGN KEY (unit_id) REFERENCES units(unit_id)
);


CREATE TABLE if not exists stock_of_wells (
    id SERIAL,
    h_date DATE NOT NULL,
    period_type VARCHAR(50) NOT NULL,
    project_id INT NOT NULL,
    total INT,  
    old_total INT,  
    active INT,  
    work INT,  
    avg_duration INTERVAL,
    commentary TEXT,
    CONSTRAINT pk_stock_of_wells PRIMARY KEY (id),
    CONSTRAINT fk_stock_of_wells_project_id FOREIGN KEY (project_id) REFERENCES projects(project_id)
);


CREATE TABLE if not exists pressure(
    id SERIAL,
    h_date DATE NOT NULL,
    period_type VARCHAR(50) NOT NULL,
    project_id INT NOT NULL,
    total INT,  
    old_total INT,  
    active INT,  
    work INT,  
    avg_duration INTERVAL,
    commentary TEXT,
    CONSTRAINT pk_stock_of_wells PRIMARY KEY (id),
    CONSTRAINT fk_stock_of_wells_project_id FOREIGN KEY (project_id) REFERENCES projects(project_id)
);


create table if not exists periods (
	period_id serial not null,
	period_name varchar(10) not null,
	CONSTRAINT pk_periods PRIMARY KEY (period_id)
);


ALTER TABLE public.commercial_data RENAME COLUMN period_type TO period_id;
ALTER TABLE public.commercial_data ALTER COLUMN period_id TYPE int USING period_id::int;
ALTER TABLE public.commercial_data ADD CONSTRAINT commercial_data_periods_fk FOREIGN KEY (period_id) REFERENCES public.periods(period_id);

ALTER TABLE public.commercial_data_nomination RENAME COLUMN period_type TO period_id;
ALTER TABLE public.commercial_data_nomination ALTER COLUMN period_id TYPE int USING period_id::int;
ALTER TABLE public.commercial_data_nomination ADD CONSTRAINT commercial_data_nomination_periods_fk FOREIGN KEY (period_id) REFERENCES public.periods(period_id);


ALTER TABLE public.commercial_data_plan RENAME COLUMN period_type TO period_id;
ALTER TABLE public.commercial_data_plan ALTER COLUMN period_id TYPE int USING period_id::int;
ALTER TABLE public.commercial_data_plan ADD CONSTRAINT commercial_data_plan_periods_fk FOREIGN KEY (period_id) REFERENCES public.periods(period_id);

ALTER TABLE public.consumption_data RENAME COLUMN period_type TO period_id;
ALTER TABLE public.consumption_data ALTER COLUMN period_id TYPE int USING period_id::int;
ALTER TABLE public.consumption_data ADD CONSTRAINT consumption_data_periods_fk FOREIGN KEY (period_id) REFERENCES public.periods(period_id);

ALTER TABLE public.stock_of_wells RENAME COLUMN period_type TO period_id;
ALTER TABLE public.stock_of_wells ALTER COLUMN period_id TYPE int USING period_id::int;
ALTER TABLE public.stock_of_wells ADD CONSTRAINT stock_of_wells_periods_fk FOREIGN KEY (period_id) REFERENCES public.periods(period_id);


ALTER TABLE public.water_stats RENAME COLUMN period_type TO period_id;
ALTER TABLE public.water_stats ALTER COLUMN period_id TYPE int USING period_id::int;
ALTER TABLE public.water_stats ADD CONSTRAINT water_stats_periods_fk FOREIGN KEY (period_id) REFERENCES public.periods(period_id);


