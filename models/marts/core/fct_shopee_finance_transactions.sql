with shopee_finance_transactions as (
    select * from {{ ref('stg_shopee_finance_transactions' )}}
),

shops as (
    select * from {{ ref('stg_shops' )}}
),

fct_shopee_finance_transactions as (
    select
        plt.sc_id as SC_ID,
        transaction_list.value:amount as amount,
        DATE(transaction_list.value:create_time) as txn_date,
        transaction_list.value:buyer_name as buyer_name,
        transaction_list.value:current_balance as current_balance,
        transaction_list.value:description as description,
        transaction_list.value:is_shop_active as is_shop_active,
        transaction_list.value:order_sn as PLFM_ORD_NO,
        transaction_list.value:pay_order_list as pay_order_list,
        transaction_list.value:reason as reason,
        transaction_list.value:refund_sn as refund_sn,
        transaction_list.value:status as status,
        transaction_list.value:transaction_fee as txn_fee,
        transaction_list.value:transaction_id as txn_id,
        transaction_list.value:transaction_type as txn_type,
        transaction_list.value:wallet_type as wallet_type,
        transaction_list.value:withdrawal_type as withdrawal_type,
        TO_JSON(TO_VARIANT({ 'record_content':a.record_content, 'record_metadata': a.record_metadata}))::variant as raw_json
    from shopee_finance_transactions a
    LEFT JOIN (SELECT * FROM shops) as plt ON plt.sc_id = a.record_metadata:key:shop_id,
    LATERAL FLATTEN (input => a.RECORD_CONTENT:response:transaction_list) as transaction_list
)

select * from fct_shopee_finance_transactions