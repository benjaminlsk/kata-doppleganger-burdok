import { afterEach, beforeAll, expect, test } from "@jest/globals"
import { DiscountApplier, Notifier } from "../discount-applier"
import { User } from "../user"

const globalThis: any = global

beforeAll(() => {
  const notifier: Notifier = {
    notify: (user: User, message: string) => {
      globalThis.notified.push({ user, message })
    }
  }
  const discountApplier = new DiscountApplier(notifier)
  const user: User = { name: "John", email: "john@dax.com" }

  globalThis.discountApplier = discountApplier
  globalThis.user = user
  globalThis.notified = []
})

afterEach(() => {
  globalThis.notified = []
})

test('apply v1', () => {
  // TODO: write a test that fails due to the bug in
  // DiscountApplier.applyV1
  const user2: User = { name: "John", email: "john@dax.com" }

  globalThis.discountApplier.applyV1(10, [globalThis.user, user2])

  expect(globalThis.notified).toHaveLength(2)
})

test('apply v2', () => {
  // TODO: write a test that fails due to the bug in
  // DiscountApplier.applyV2
  const users: User[] = [
    { name: "Emily", email: "emily@paris.com" },
    globalThis.user,
  ]

  globalThis.discountApplier.applyV2(10, [users])

  expect(globalThis.notified).toHaveLength(2)

  users.forEach((user, index) => {
    expect(globalThis.notified[index]).toContainEqual({
      user,
      message: `You've got a new discount of 10%`,
    })
  })
})
