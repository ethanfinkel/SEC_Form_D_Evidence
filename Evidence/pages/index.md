---
title: VC Fundraising
---

```sql vc_data
  select
      ENTITYNAME, sum(TOTALAMOUNTSOLD)
  from vc_data.vc_data
  group by ENTITYNAME
  order by 2 desc
  limit 1000
  
```


<Dropdown data={vc_data} name=ENTITYNAME value=ENTITYNAME>
    <DropdownOption value="%" valueLabel="All Firms"/>
</Dropdown>

<Dropdown name=year default=%>
    <DropdownOption value=% valueLabel="All Years" order={1}/>
    <DropdownOption value=2019/>
    <DropdownOption value=2020/>
    <DropdownOption value=2021/>
    <DropdownOption value=2022/>
    <DropdownOption value=2023/>
    <DropdownOption value=2024/>
</Dropdown>

```sql data_raised_by_firm
  select 
      date_trunc('month', normalized_date::DATE) as month,
      ENTITYNAME,
      sum(TOTALAMOUNTSOLD) as total_raised,
  from vc_data.vc_data
  where ENTITYNAME like '${inputs.ENTITYNAME.value}'
  and date_part('year', normalized_date::DATE) like '${inputs.year.value}' 
  and INVESTMENTFUNDTYPE = 'Venture Capital Fund'
  group by all
  order by total_raised desc
  limit 10000
```

<BarChart
    data={data_raised_by_firm}
    title="Raised by year, {inputs.year.label}"
    x=month
    y=total_raised
    yFmt=usd2b
/>

```sql heatmap
  select 
      normalized_date::DATE as date,
      sum(TOTALAMOUNTSOLD) as total_raised,
  from vc_data.vc_data
  where ENTITYNAME like '${inputs.ENTITYNAME.value}'
  and date_part('year', normalized_date::DATE) like '${inputs.year.value}' 
  and INVESTMENTFUNDTYPE = 'Venture Capital Fund'
  group by all
```

<CalendarHeatmap
    data={heatmap}
    date=date
    value=total_raised
    valueFmt=usd 
    connectGroup=group1
/>

```sql datatable
  select 
      normalized_date::DATE as date,
      ENTITYNAME,
      fund_name,
      sum(TOTALAMOUNTSOLD) as total_raised,
  from vc_data.vc_data
  where ENTITYNAME like '${inputs.ENTITYNAME.value}'
  and date_part('year', normalized_date::DATE) like '${inputs.year.value}' 
  and INVESTMENTFUNDTYPE = 'Venture Capital Fund'
  group by all
  order by total_raised desc
```

<DataTable data={datatable}>
  <Column id=date  />
  <Column id=ENTITYNAME  />
  <Column id=fund_name  />
  <Column id=total_raised  fmt=usd1m/>
</DataTable>`


```sql chart_query
  select 
      ENTITYNAME,
      sum(TOTALAMOUNTSOLD) as total_raised,
  from vc_data.vc_data
  where ENTITYNAME like '${inputs.ENTITYNAME.value}'
  and INVESTMENTFUNDTYPE = 'Venture Capital Fund'
  group by all
  order by total_raised desc
  limit 100
```

<BarChart
    data={chart_query}
    title="All Time Raised"
    x=ENTITYNAME
    y=total_raised
    swapXY=true
/>
