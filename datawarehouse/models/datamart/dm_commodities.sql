with commodities as (
    select
        date,
        symbol,
        cast(close_value as double precision) as close_value
    from 
        {{ ref ('stg_commodities') }}
),

movimentacao as (
    select
        date,
        symbol,
        action,
        cast(quantity as double precision) as quantity
    from 
        {{ ref ('stg_commodities_moviment') }}
),

joined as (
    select
        c.date,
        c.symbol,
        c.close_value,
        m.action,
        m.quantity,
        (m.quantity * c.close_value) as valor,
        case
            when m.action = 'sell' then (m.quantity * c.close_value)
            else -(m.quantity * c.close_value)
        end as ganho
    from
        commodities c
    inner join
        movimentacao m
    on
        c.date = m.date
        and c.symbol = m.symbol
),

last_day as (
    select
        max(date) as max_date
    from
        joined
),

filtered as (
    select
        *
    from
        joined
    where
        date = (select max_date from last_day)
)

select
    date,
    symbol,
    close_value,
    action,
    quantity,
    valor,
    ganho
from
    filtered