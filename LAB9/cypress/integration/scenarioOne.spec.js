describe('Scenario One', () => {
    beforeEach(() => {
    cy.visit('https://www.saucedemo.com/')
    })

    it('should load the page successfully', () => {
    cy.title().should('equal', 'Swag Labs')
    cy.get('.login_logo').should('be.visible')
    cy.get('.login_wrapper').should('be.visible')
    cy.get('.login_credentials_wrap').should('be.visible')
})
})