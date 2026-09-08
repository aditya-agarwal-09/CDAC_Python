from copy import deepcopy


class AccountNotFoundError(Exception):
    pass


class OverdraftError(Exception):
    pass


class InvalidTransactionError(Exception):
    pass


def process_transaction_batch(accounts, batch_list, log_path):
  
    backup = deepcopy(accounts)

    try:
        for transaction in batch_list:
            acc = transaction["acc"]
            transaction_type = transaction["type"]
            amt = transaction["amt"]

         
            if acc not in accounts:
                raise AccountNotFoundError(
                    f"Account '{acc}' not found."
                )

         
            if transaction_type not in ("deposit", "withdraw"):
                raise InvalidTransactionError(
                    f"Invalid transaction type '{transaction_type}'."
                )

           
            if amt <= 0:
                raise InvalidTransactionError(
                    "Transaction amount must be positive."
                )

        
            if transaction_type == "deposit":
                accounts[acc] += amt

            elif transaction_type == "withdraw":
                if accounts[acc] < amt:
                    raise OverdraftError(
                        f"Insufficient funds. Account {acc} has balance "
                        f"{accounts[acc]}, requested {amt}."
                    )

                accounts[acc] -= amt

    except Exception as exc:

        accounts.clear()
        accounts.update(deepcopy(backup))

        with open(log_path, "a") as log_file:
            log_file.write(
                f"[ROLLBACK] Batch aborted: "
                f"{type(exc).__name__} - {exc}\n"
            )
        raise

    with open(log_path, "a") as log_file:
        log_file.write(
            f"[SUCCESS] Batch completed. "
            f"{len(batch_list)} transaction(s) processed.\n"
        )

    return accounts

accounts = {"ACC01": 100.0, "ACC02": 50.0}
log_file = "transactions.log"

batch_1 = [
    {"acc": "ACC01", "type": "withdraw", "amt": 30.0},
    {"acc": "ACC02", "type": "deposit", "amt": 20.0}
]

accounts = process_transaction_batch(accounts, batch_1, log_file)

print(accounts)


batch_2 = [
    {"acc": "ACC01", "type": "deposit", "amt": 50.0},
    {"acc": "ACC02", "type": "withdraw", "amt": 200.0}
]

try:
    accounts = process_transaction_batch(accounts, batch_2, log_file)
except OverdraftError as e:
    print(f"Caught: {e}")

print(accounts)
