SELECT
  month AS processing_date,
  practice AS practice_id,
  SUBSTR(bnf_code, 1, 9) AS chemical_id,
  SUM(items) AS items,
  SUM(actual_cost) AS cost,
  CAST(SUM(quantity) AS INT64) AS quantity
FROM
  ebmdatalab.%s.prescribing
GROUP BY
  processing_date,
  practice_id,
  chemical_id