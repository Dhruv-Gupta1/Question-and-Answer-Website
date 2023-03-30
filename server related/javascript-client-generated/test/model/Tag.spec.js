/*
 * queriKorner - OpenAPI 3.0
 * This is the API documentation of the queriKorner server application. It is based on the OpenAPI 3.0 specification.
 *
 * OpenAPI spec version: 1.0.11
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 3.0.41
 *
 * Do not edit the class manually.
 *
 */
(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.QueriKornerOpenApi30);
  }
}(this, function(expect, QueriKornerOpenApi30) {
  'use strict';

  var instance;

  describe('(package)', function() {
    describe('Tag', function() {
      beforeEach(function() {
        instance = new QueriKornerOpenApi30.Tag();
      });

      it('should create an instance of Tag', function() {
        // TODO: update the code to test Tag
        expect(instance).to.be.a(QueriKornerOpenApi30.Tag);
      });

      it('should have the property tagId (base name: "tagId")', function() {
        // TODO: update the code to test the property tagId
        expect(instance).to.have.property('tagId');
        // expect(instance.tagId).to.be(expectedValueLiteral);
      });

      it('should have the property name (base name: "Name")', function() {
        // TODO: update the code to test the property name
        expect(instance).to.have.property('name');
        // expect(instance.name).to.be(expectedValueLiteral);
      });

      it('should have the property numberOfQuestions (base name: "NumberOfQuestions")', function() {
        // TODO: update the code to test the property numberOfQuestions
        expect(instance).to.have.property('numberOfQuestions');
        // expect(instance.numberOfQuestions).to.be(expectedValueLiteral);
      });

      it('should have the property description (base name: "description")', function() {
        // TODO: update the code to test the property description
        expect(instance).to.have.property('description');
        // expect(instance.description).to.be(expectedValueLiteral);
      });

    });
  });

}));
