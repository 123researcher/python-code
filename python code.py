import simplify
 
simplify.public_key = "YOUR_PUBLIC_API_KEY"
simplify.private_key = "YOUR_PRIVATE_API_KEY"
 
plan = simplify.Plan.create({
        "amount" : "1000",
        "billingCycleLimit" : "4",
        "billingCycle" : "FIXED",
        "renewalReminderLeadDays" : "7",
        "name" : "plan2",
        "frequencyPeriod" : "2",
        "frequency" : "WEEKLY"
 
})
 
print(plan)

import simplify
 
simplify.public_key = "YOUR_PUBLIC_API_KEY"
simplify.private_key = "YOUR_PRIVATE_API_KEY"
 
customer = simplify.Customer.create({
        "reference" : "Ref1",
        "subscriptions" : [
           {
              "plan" : "[PLAN ID]"
           }
        ],
        "name" : "Customer Customer",
        "email" : "customer@mastercard.com",
        "card" : {
           "number" : "5555555555554444",
           "expMonth" : "11",
           "cvc" : "123",
           "expYear" : "35"
        }
 
})
 
print(customer)


import simplify
 
simplify.public_key = "YOUR_PUBLIC_API_KEY"
simplify.private_key = "YOUR_PRIVATE_API_KEY"
 
invoiceItem = simplify.InvoiceItem.create({
        "reference" : "ref111",
        "amount" : "1000",
        "description" : "Invoice Item1",
        "invoice" : "[INVOICE ID]"
 
})
 
print(invoiceItem)
This adds a one time payment of $10 USD to the customer's next invoice.




import simplify
 
simplify.public_key = "YOUR_PUBLIC_API_KEY"
simplify.private_key = "YOUR_PRIVATE_API_KEY"
 
coupon = simplify.Coupon.create({
        "maxRedemptions" : "100",
        "endDate" : "64063288800000",
        "percentOff" : "20",
        "description" : "20% off!",
        "couponCode" : "20off",
        "startDate" : "2394829384000"
 
})
 
print(coupon)




import simplify
 
simplify.public_key = "YOUR_PUBLIC_API_KEY"
simplify.private_key = "YOUR_PRIVATE_API_KEY"
 
subscription = simplify.Subscription.create({
        "coupon" : "[COUPON ID]",
        "plan" : "[PLAN ID]",
        "customer" : "[CUSTOMER ID]"
 
})
 
print(subscription)



import simplify
 
simplify.public_key = "YOUR_PUBLIC_API_KEY"
simplify.private_key = "YOUR_PRIVATE_API_KEY"
 
refund = simplify.Refund.create({
        "reference" : "76398734634",
        "reason" : "Refund Description",
        "amount" : "100",
        "payment" : "[PAYMENT ID]"
 
})
 
print(refund)



import simplify
 
simplify.public_key = "YOUR_PUBLIC_API_KEY"
simplify.private_key = "YOUR_PRIVATE_API_KEY"
 
authorization = simplify.Authorization.create({
        "reference" : "7a6ef6be31",
        "amount" : "1000",
        "description" : "payment description",
        "currency" : "USD",
        "token" : "[TOKEN ID]"
 
})
 
print(authorization)

import simplify
 
simplify.public_key = "YOUR_PUBLIC_API_KEY"
simplify.private_key = "YOUR_PRIVATE_API_KEY"
 
payment = simplify.Payment.create({
        "authorization" : "[AUTHORIZATION ID]",
        "reference" : "BCK2THEST",
        "amount" : "2500",
        "description" : "shipment of two eggs in a glass bottle",
        "currency" : "USD",
        "replayId" : "A-77633219"
 
})
 
if payment.paymentStatus == 'APPROVED':
    print("Payment approved")


    import simplify
 
simplify.public_key = "YOUR_PUBLIC_API_KEY"
simplify.private_key = "YOUR_PRIVATE_API_KEY"
 
authorization = simplify.Authorization.find('4TR6Bc')
authorization.delete()

