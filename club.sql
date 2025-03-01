-- Create Members table
CREATE TABLE Members (
    members_id INT AUTO_INCREMENT PRIMARY KEY,
    members_name VARCHAR(100) NOT NULL,
    members_date_of_birth DATE,
    members_phone_number VARCHAR(20),
    members_gender ENUM('Male', 'Female', 'Other'),
    members_email VARCHAR(100),
    members_preferences TEXT
);

-- Create Location table
CREATE TABLE Location (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    capacity INT,
    type VARCHAR(50),
    availability BOOLEAN
);

-- Create Activity table
CREATE TABLE Activity (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,
    activity_name VARCHAR(100) NOT NULL,
    description TEXT,
    activity_status ENUM('Active', 'Inactive', 'Cancelled') NOT NULL,
    participation_quota INT,
    location_id INT,
    FOREIGN KEY (location_id) REFERENCES Location(location_id)
);

-- Create Signup table
CREATE TABLE Signup (
    signup_id INT AUTO_INCREMENT PRIMARY KEY,
    members_id INT,
    activity_id INT,
    signup_date DATE,
    signup_time TIME,
    FOREIGN KEY (members_id) REFERENCES Members(members_id),
    FOREIGN KEY (activity_id) REFERENCES Activity(activity_id)
);

-- Create Feedback table
CREATE TABLE Feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    activity_id INT,
    members_id INT,
    rating INT,
    comments TEXT,
    feedback_date DATE,
    FOREIGN KEY (activity_id) REFERENCES Activity(activity_id),
    FOREIGN KEY (members_id) REFERENCES Members(members_id)
);

-- Add MembershipType table
CREATE TABLE MembershipType (
    membership_type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL,
    description TEXT,
    fee DECIMAL(10, 2)
);

-- Modify Members table to include membership type
ALTER TABLE Members ADD COLUMN membership_type_id INT;
ALTER TABLE Members ADD FOREIGN KEY (membership_type_id) REFERENCES MembershipType(membership_type_id);

-- Insert sample data
INSERT INTO MembershipType (type_name, description, fee) VALUES
('Standard', 'Basic membership with access to most facilities', 50.00),
('Premium', 'Full access to all facilities and priority booking', 100.00);

INSERT INTO Members (members_name, members_date_of_birth, members_phone_number, members_gender, members_email, members_preferences, membership_type_id) VALUES
('John Doe', '1990-05-15', '1234567890', 'Male', 'john@example.com', 'Swimming, Tennis', 1),
('Jane Smith', '1985-08-22', '9876543210', 'Female', 'jane@example.com', 'Yoga, Running', 2);

INSERT INTO Location (capacity, type, availability) VALUES
(50, 'Indoor Gym', TRUE),
(100, 'Swimming Pool', TRUE);

INSERT INTO Activity (activity_name, description, activity_status, participation_quota, location_id) VALUES
('Morning Yoga', 'Start your day with relaxing yoga', 'Active', 20, 1),
('Swim Class', 'Learn to swim or improve your technique', 'Active', 15, 2);

INSERT INTO Signup (members_id, activity_id, signup_date, signup_time) VALUES
(1, 1, '2024-10-15', '09:00:00'),
(2, 2, '2024-10-16', '14:00:00');

INSERT INTO Feedback (activity_id, members_id, rating, comments, feedback_date) VALUES
(1, 1, 5, 'Great yoga class!', '2024-10-16'),
(2, 2, 4, 'Enjoyed the swim class, but pool was a bit crowded', '2024-10-17');


-- 1. Basic query: List all members
SELECT * FROM Members;

-- 2. Join query: Get all activities and their locations
SELECT a.activity_name, l.type AS location_type
FROM Activity a
JOIN Location l ON a.location_id = l.location_id;

-- 3. Aggregate query: Count members by gender
SELECT members_gender, COUNT(*) AS member_count
FROM Members
GROUP BY members_gender;

-- 4. Subquery: Find members who have signed up for activities in the last 7 days
SELECT m.members_name
FROM Members m
WHERE m.members_id IN (
    SELECT s.members_id
    FROM Signup s
    WHERE s.signup_date >= CURDATE() - INTERVAL 7 DAY
);

-- 5. Multiple table join: Get activity details with signup count and average rating
SELECT a.activity_name, 
       COUNT(DISTINCT s.members_id) AS signup_count, 
       AVG(f.rating) AS avg_rating
FROM Activity a
LEFT JOIN Signup s ON a.activity_id = s.activity_id
LEFT JOIN Feedback f ON a.activity_id = f.activity_id
GROUP BY a.activity_id;

-- 6. Update query: Change activity status to 'Inactive' for activities with no signups
UPDATE Activity a
SET a.activity_status = 'Inactive'
WHERE a.activity_id NOT IN (SELECT DISTINCT activity_id FROM Signup);

-- 7. Delete query: Remove old feedback (more than 1 year old)
DELETE FROM Feedback
WHERE feedback_date < DATE_SUB(CURDATE(), INTERVAL 1 YEAR);

-- 8. Complex query: Find the most popular activity (most signups) for each location
SELECT l.type AS location_type, a.activity_name, signup_count
FROM Location l
JOIN Activity a ON l.location_id = a.location_id
JOIN (
    SELECT activity_id, COUNT(*) AS signup_count
    FROM Signup
    GROUP BY activity_id
) s ON a.activity_id = s.activity_id
WHERE (l.location_id, s.signup_count) IN (
    SELECT a2.location_id, MAX(s2.signup_count)
    FROM Activity a2
    JOIN (
        SELECT activity_id, COUNT(*) AS signup_count
        FROM Signup
        GROUP BY activity_id
    ) s2 ON a2.activity_id = s2.activity_id
    GROUP BY a2.location_id
);

-- 9. Analytical query: Rank members by the number of activities they've signed up for
SELECT m.members_name, 
       COUNT(s.activity_id) AS activity_count,
       RANK() OVER (ORDER BY COUNT(s.activity_id) DESC) AS rank
FROM Members m
LEFT JOIN Signup s ON m.members_id = s.members_id
GROUP BY m.members_id
ORDER BY rank;

-- 10. Time-based query: Get the busiest day of the week for signups
SELECT DAYNAME(signup_date) AS day_of_week, 
       COUNT(*) AS signup_count
FROM Signup
GROUP BY day_of_week
ORDER BY signup_count DESC
LIMIT 1;

-- 11. Add operation: register a new event for a member and automatically update the number of participants in the event
INSERT INTO Signup (members_id, activity_id, signup_date, signup_time)
VALUES (1, 3, CURDATE(), CURTIME());

UPDATE Activity a
SET a.participation_quota = a.participation_quota - 1
WHERE a.activity_id = 3
  AND a.participation_quota > 0;

-- 12. Delete operation: cancellation of expired and unregistered events and deletion of the related location booking
DELETE FROM Activity
WHERE activity_id IN (
    SELECT a.activity_id
    FROM (SELECT * FROM Activity) AS a
    LEFT JOIN Signup s ON a.activity_id = s.activity_id
    WHERE s.signup_id IS NULL
      AND a.activity_status = 'Active'
      AND EXISTS (
          SELECT 1
          FROM Location l
          WHERE l.location_id = a.location_id
            AND l.availability = FALSE
      )
);

UPDATE Location l
SET l.availability = TRUE
WHERE l.location_id NOT IN (
    SELECT DISTINCT location_id
    FROM Activity
    WHERE activity_status = 'Active'
);

-- 13. Find actions: find the most popular membership types and their related activities
SELECT mt.type_name, COUNT(DISTINCT s.members_id) as member_count, 
       GROUP_CONCAT(DISTINCT a.activity_name) as popular_activities
FROM MembershipType mt
JOIN Members m ON mt.membership_type_id = m.membership_type_id
JOIN Signup s ON m.members_id = s.members_id
JOIN Activity a ON s.activity_id = a.activity_id
GROUP BY mt.membership_type_id
ORDER BY member_count DESC
LIMIT 1;

-- 14. Update operation: Adjust activity status and description based on member feedback
UPDATE Activity a
JOIN (
    SELECT activity_id, AVG(rating) as avg_rating
    FROM Feedback
    GROUP BY activity_id
) f ON a.activity_id = f.activity_id
SET a.activity_status = CASE
    WHEN f.avg_rating < 2 THEN 'Inactive'
    WHEN f.avg_rating >= 4 THEN 'Active'
    ELSE a.activity_status
END,
a.description = CASE
    WHEN f.avg_rating < 2 THEN CONCAT(a.description, ' (Currently under review based on feedback)')
    WHEN f.avg_rating >= 4 THEN CONCAT(a.description, ' (Highly rated activity!)')
    ELSE a.description
END
WHERE f.avg_rating IS NOT NULL;

-- 15. Complex query operation: generating monthly activity reports, including activity statistics and top participants
WITH monthly_activity AS (
    SELECT 
        DATE_FORMAT(s.signup_date, '%Y-%m') AS month,
        a.activity_id,
        a.activity_name,
        COUNT(DISTINCT s.members_id) AS participant_count
    FROM Activity a
    JOIN Signup s ON a.activity_id = s.activity_id
    GROUP BY month, a.activity_id
),
top_participants AS (
    SELECT 
        DATE_FORMAT(s.signup_date, '%Y-%m') AS month,
        m.members_name,
        COUNT(DISTINCT s.activity_id) AS activity_count,
        ROW_NUMBER() OVER (PARTITION BY DATE_FORMAT(s.signup_date, '%Y-%m') ORDER BY COUNT(DISTINCT s.activity_id) DESC) AS rank
    FROM Members m
    JOIN Signup s ON m.members_id = s.members_id
    GROUP BY month, m.members_id
)
SELECT 
    ma.month,
    COUNT(DISTINCT ma.activity_id) AS total_activities,
    SUM(ma.participant_count) AS total_participants,
    GROUP_CONCAT(DISTINCT CONCAT(ma.activity_name, ': ', ma.participant_count) ORDER BY ma.participant_count DESC SEPARATOR '; ') AS activity_breakdown,
    GROUP_CONCAT(DISTINCT CONCAT(tp.members_name, ' (', tp.activity_count, ' activities)') ORDER BY tp.activity_count DESC SEPARATOR ', ') AS top_3_participants
FROM monthly_activity ma
LEFT JOIN top_participants tp ON ma.month = tp.month AND tp.rank <= 3
GROUP BY ma.month
ORDER BY ma.month DESC;