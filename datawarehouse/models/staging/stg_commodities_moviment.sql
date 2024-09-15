with source as (
    select
        date,
        symbol,
        action,
        quantity
    from 
        {{ source('dbwarehouse_wlm7', 'commodities_moviment') }}
),

renamed as (
    select
        cast(date as date),
        symbol,
        action,
        quantity
    from source
)

select * from renamed