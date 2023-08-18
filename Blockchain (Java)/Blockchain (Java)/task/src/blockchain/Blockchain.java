package blockchain;

import java.util.Date;

public class Blockchain {
    public static void main(String[] args) {
        long timeStamp;
        String previousHash = "0";
        for (int i = 1; i <= 5; i++) {
            timeStamp = new Date().getTime();
            System.out.println("Block:");
            System.out.println("Id: " + i);
            System.out.println("Timestamp: " + timeStamp);
            System.out.println("Hash of the previous block: ");
            System.out.println(previousHash);
            System.out.println("Hash of the block: ");
            Block block = new Block(i, timeStamp, previousHash);
            String hashBlock = block.calculateHash();
            System.out.println(hashBlock + "\n");
            previousHash = hashBlock;
        }

    }
}
