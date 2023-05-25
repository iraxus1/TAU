describe('Scenario Three', () => {
    beforeEach(() => {
    cy.visit('https://www.saucedemo.com/')
    })
    
    it('should log in and perform additional feature', () => {
    cy.get('#user-name').type('standard_user')
    cy.get('#password').type('secret_sauce')
    cy.get('#login-button').click()
    cy.url().should('include', 'inventory.html')
    cy.get('.inventory_item_name')
  .should('have.length', 1)
  .and('contain', 'Sauce Labs Backpack')

    cy.get('.inventory_item_price')
    .should('have.length', 1)
    .and('contain', '$29.99')
})
})
