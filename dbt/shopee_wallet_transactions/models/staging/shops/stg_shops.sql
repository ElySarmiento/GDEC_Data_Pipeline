{{ config(tags=['shopee_wallet_transactions']) }}
select * from {{ source('shops', 'MKTP_ACCT_DT_V2') }}