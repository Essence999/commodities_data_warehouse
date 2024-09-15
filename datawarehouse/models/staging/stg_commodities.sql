with source as (
select "date", "Close", "symbol"
from {{ source('dbwarehouse_wlm7', 'commodities') }}

),

renamed as (
    select cast("date" as date) as data, "Close" as close_value, symbol
    from source
    )

select * from renamed