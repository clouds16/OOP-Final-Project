

function addPizzaSection() {

    let form_element = '<select id="pizza" name="pizzas"> <option value="peperoni">  Peperoni </option> <option value="cheese"> Cheese </option> <option value="pesto"> Pesto </option> <option value="meatlovers"> MeatLovers </option> <option value="white"> Chicken </option></select> '

    document.getElementById("order-form").append(form_element)
}