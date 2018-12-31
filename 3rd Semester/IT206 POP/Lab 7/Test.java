import java.awt.Color;
import java.awt.Dimension;
import java.awt.EventQueue;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.Timer;
import javax.swing.UIManager;
import javax.swing.UnsupportedLookAndFeelException;

public class Test {

    public static void main(String[] args) {
        new Test();
    }

    public Test() {
        EventQueue.invokeLater(new Runnable() {
            @Override
            public void run() {
                try {
                    UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
                } catch (ClassNotFoundException | InstantiationException | IllegalAccessException | UnsupportedLookAndFeelException ex) {
                    ex.printStackTrace();
                }

                JFrame frame = new JFrame("Testing");
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                frame.add(new TestPane());
                frame.pack();
                frame.setLocationRelativeTo(null);
                frame.setVisible(true);
            }
        });
    }

    public class TestPane extends JPanel {

        private Truck truck;

        public TestPane() {
            truck = new Truck();
            Timer timer = new Timer(40, new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    truck.update(getSize());
                    repaint();
                }
            });
            timer.start();
        }

        @Override
        public Dimension getPreferredSize() {
            return new Dimension(200, 200);
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2d = (Graphics2D) g.create();
            truck.paint(g2d);
            g2d.dispose();
        }

    }

    public class Truck {

        private int x, y;
        // I had to calculate these
        private int width = 85;
        private int height = 65;

        private int xDelta = 4;

        private int xOverFlow = 0;

        public void update(Dimension bounds) {
            x += xDelta;
            if (x > bounds.width) {
                x = 0;
            }

            if (x + width > bounds.width) {
                xOverFlow = (x + width) - bounds.width;
            } else {
                xOverFlow = -1;
            }
        }

        public void paint(Graphics2D g) {
            Graphics2D g2d = (Graphics2D) g.create();
            g2d.translate(x, y);
            paintTruck(g2d);
            g2d.dispose();

            if (xOverFlow > 0) {
                g2d = (Graphics2D) g.create();
                g2d.translate(xOverFlow - width, y);
                paintTruck(g2d);
                g2d.dispose();
            }
        }

        protected void paintTruck(Graphics2D g2d) {
            g2d.setColor(Color.gray);
            g2d.fillRect(0, 10, 70, 45);
            g2d.setColor(Color.yellow);
            g2d.fillRoundRect(50, 15, 35, 35, 10, 10);
            g2d.setColor(Color.black);
            g2d.fillArc(5, 50, 10, 10, 0, 360);
            g2d.fillArc(55, 50, 10, 10, 0, 360);

            g2d.setColor(Color.gray);
            g2d.fillRect(0, 10, 70, 45);
            g2d.setColor(Color.yellow);
            g2d.fillRoundRect(50, 15, 35, 35, 10, 10);
            g2d.setColor(Color.black);
            g2d.fillArc(5, 50, 10, 10, 0, 360);
            g2d.fillArc(55, 50, 10, 10, 0, 360);
        }
    }

}