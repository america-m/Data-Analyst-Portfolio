public class MenuItem extends Menu{

    private String menuItem;
    private int itemPrice;
    private String itemDescription;

    public void setMenuItem(String menuItem, int itemPrice, String itemDescription) {
        this.menuItem = menuItem;
        this.itemPrice = itemPrice;
        this.itemDescription = itemDescription;
    }
    public String getMenuItem() {
        return menuItem;
    }

    public int getItemPrice() {
        return itemPrice;
    }

    public String getItemDescription() {
        return itemDescription;
    }

    public void display()
    {
        System.out.println(menuItem + itemPrice + itemDescription);
    }
}


